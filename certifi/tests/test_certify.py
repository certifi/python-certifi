import os
import threading
import unittest

import certifi
import certifi.core


class TestCertifi(unittest.TestCase):
    def test_cabundle_exists(self) -> None:
        assert os.path.exists(certifi.where())

    def test_read_contents(self) -> None:
        content = certifi.contents()
        assert "-----BEGIN CERTIFICATE-----" in content

    def test_py_typed_exists(self) -> None:
        assert os.path.exists(
            os.path.join(os.path.dirname(certifi.__file__), 'py.typed')
        )


class TestWhereThreadSafety(unittest.TestCase):
    """where() must materialise the CA bundle exactly once.

    The `if _CACERT_PATH is None` test and the assignment that publishes the
    path are separate operations, so concurrent callers could each enter their
    own resource context and register their own atexit hook while only the
    last _CACERT_CTX assignment survived, orphaning the others. Under
    zipimport as_file() extracts a temporary file, so an orphaned context is a
    file nothing will clean up.
    """

    def test_where_enters_the_resource_context_once(self) -> None:
        core = certifi.core
        if not hasattr(core, "_CACERT_PATH"):
            self.skipTest("this build of certifi does not lazily materialise the bundle")

        original = (core._CACERT_PATH, core._CACERT_CTX, core.atexit.register)
        registrations = []
        lock = threading.Lock()

        def counting_register(func, *args, **kwargs):
            # Count rather than call through, so the test does not pile up real
            # atexit hooks.
            with lock:
                registrations.append(func)

        n_threads = 4
        go = threading.Event()
        results: list[str] = []

        try:
            core.atexit.register = counting_register

            for _ in range(50):
                core._CACERT_PATH = None
                core._CACERT_CTX = None
                registrations.clear()
                results.clear()

                def worker() -> None:
                    # An Event rather than a Barrier, so a runner that can only
                    # give us some of the threads still runs.
                    go.wait()
                    path = core.where()
                    with lock:
                        results.append(path)

                threads = []
                for _ in range(n_threads):
                    thread = threading.Thread(target=worker)
                    try:
                        thread.start()
                    except RuntimeError:
                        break
                    threads.append(thread)

                if len(threads) < 2:
                    go.set()
                    for thread in threads:
                        thread.join()
                    self.skipTest("could not start enough threads to test for the race")

                go.set()
                for thread in threads:
                    thread.join()
                go.clear()

                self.assertEqual(len(registrations), 1)
                self.assertEqual(len(set(results)), 1)
        finally:
            go.set()
            core._CACERT_PATH, core._CACERT_CTX, core.atexit.register = original
