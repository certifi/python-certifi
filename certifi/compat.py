"""
Fallback for Python prior to 3.9 where importlib_resources
is not available.
Does not support modules where __file__ is not defined on
the module.
"""

import os


def read_text(_module, _path):
    with open(where(), "r", encoding="ascii") as data:
        return data.read()


def where():
    return os.path.join(os.path.dirname(__file__), "cacert.pem")
