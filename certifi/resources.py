import atexit
import functools

try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources


# ensure 'files' API is present
resources.files
read_text = resources.read_text


def as_file(path):
    """
    Ensure the path is a file on the file system for the duration
    of the interpreter run.
    """
    ctx = resources.as_file(path)
    tmp_copy = ctx.__enter__()
    atexit.register(tmp_copy.__exit__, None, None, None)
    return tmp_copy


@functools.lru_cache()
def where():
    return as_file(resources.files('certifi') / 'cacert.pem')
