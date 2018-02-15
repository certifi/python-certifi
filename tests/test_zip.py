import glob
import os.path
import subprocess
import tempfile
import unittest


_TEST_SCRIPT='; '.join('''import certifi
import os.path
assert os.path.exists(certifi.where()), "certs do not exist"
print "PASS"'''.split('\n'))


class TestCertifiZip(unittest.TestCase):
    def test_egg_zip(self):
        # verifies that certifi works if packaged in an egg

        # locate setup.py and build the egg
        setup_py_path = os.path.normpath(os.path.join(os.path.basename(__file__), ".."))
        subprocess.check_call(('python', 'setup.py', 'bdist_egg'), cwd=setup_py_path)

        egg_glob = os.path.join(setup_py_path, 'dist', 'certifi-*.egg')
        eggs = glob.glob(egg_glob)
        self.assertEqual(1, len(eggs))
        egg_path = os.path.abspath(eggs[0])

        # change to a different directory and set PYTHONPATH to the egg: should still be able
        # to access the certifi certificate file
        subprocess_env = dict(os.environ)
        subprocess_env['PYTHONPATH'] = egg_path

        output = subprocess.check_output(('python', '-c', _TEST_SCRIPT),
            cwd=tempfile.gettempdir(), env=subprocess_env)
        self.assertIn('PASS', output)
