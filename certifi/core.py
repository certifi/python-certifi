# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os

try:
    from importlib.resources import read_text
except ImportError:
    def read_text(_module, _path, encoding="ascii"):
        return open(where(), "r", encoding=encoding).read()


def where():
    f = os.path.dirname(__file__)

    return os.path.join(f, 'cacert.pem')


def contents():
    return read_text("certifi", "cacert.pem", encoding="ascii")
