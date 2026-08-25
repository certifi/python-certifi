"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem or its contents.
"""
import sys
import atexit
import threading

# where() lazily materialises the CA bundle and publishes it through module
# globals.  The `is None` test and the assignment are separate operations, so
# without this lock several threads can each enter the resource context and
# register their own atexit hook while only the last _CACERT_CTX assignment
# survives, orphaning the others.
_CACERT_LOCK = threading.Lock()

def exit_cacert_ctx() -> None:
    _CACERT_CTX.__exit__(None, None, None)  # type: ignore[union-attr]


if sys.version_info >= (3, 11):

    from importlib.resources import as_file, files

    _CACERT_CTX = None
    _CACERT_PATH = None

    def where() -> str:
        # This is slightly terrible, but we want to delay extracting the file
        # in cases where we're inside of a zipimport situation until someone
        # actually calls where(), but we don't want to re-extract the file
        # on every call of where(), so we'll do it once then store it in a
        # global variable.
        global _CACERT_CTX
        global _CACERT_PATH
        if _CACERT_PATH is None:
            with _CACERT_LOCK:
                if _CACERT_PATH is not None:
                    return _CACERT_PATH
                # This is slightly janky, the importlib.resources API wants you to
                # manage the cleanup of this file, so it doesn't actually return a
                # path, it returns a context manager that will give you the path
                # when you enter it and will do any cleanup when you leave it. In
                # the common case of not needing a temporary file, it will just
                # return the file system location and the __exit__() is a no-op.
                #
                # We also have to hold onto the actual context manager, because
                # it will do the cleanup whenever it gets garbage collected, so
                # we will also store that at the global level as well.
                ctx = as_file(files("certifi").joinpath("cacert.pem"))
                path = str(ctx.__enter__())
                _CACERT_CTX = ctx
                atexit.register(exit_cacert_ctx)
                # published last, so no thread can observe a path whose
                # context manager is not yet reachable for cleanup
                _CACERT_PATH = path

        return _CACERT_PATH

    def contents() -> str:
        return files("certifi").joinpath("cacert.pem").read_text(encoding="ascii")

else:

    from importlib.resources import path as get_path, read_text

    _CACERT_CTX = None
    _CACERT_PATH = None

    def where() -> str:
        # This is slightly terrible, but we want to delay extracting the
        # file in cases where we're inside of a zipimport situation until
        # someone actually calls where(), but we don't want to re-extract
        # the file on every call of where(), so we'll do it once then store
        # it in a global variable.
        global _CACERT_CTX
        global _CACERT_PATH
        if _CACERT_PATH is None:
            with _CACERT_LOCK:
                if _CACERT_PATH is not None:
                    return _CACERT_PATH
                # This is slightly janky, the importlib.resources API wants you
                # to manage the cleanup of this file, so it doesn't actually
                # return a path, it returns a context manager that will give
                # you the path when you enter it and will do any cleanup when
                # you leave it. In the common case of not needing a temporary
                # file, it will just return the file system location and the
                # __exit__() is a no-op.
                #
                # We also have to hold onto the actual context manager, because
                # it will do the cleanup whenever it gets garbage collected, so
                # we will also store that at the global level as well.
                ctx = get_path("certifi", "cacert.pem")
                path = str(ctx.__enter__())
                _CACERT_CTX = ctx
                atexit.register(exit_cacert_ctx)
                # published last, so no thread can observe a path whose
                # context manager is not yet reachable for cleanup
                _CACERT_PATH = path

        return _CACERT_PATH

    def contents() -> str:
        return read_text("certifi", "cacert.pem", encoding="ascii")
