# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem or its contents.
"""
import importlib
import os

try:
    import importlib.resources
    # Defeat lazy module importers.
    importlib.resources.open_binary
    _HAVE_RESOURCE_READER = True
except ImportError:
    _HAVE_RESOURCE_READER = False

try:
    import pkg_resources
    # Defeat lazy module importers.
    _HAVE_PKG_RESOURCES = True
except ImportError:
    _HAVE_PKG_RESOURCES = False

_PACKAGE_NAME = "certifi"
_CACERT_NAME = "cacert.pem"


def where():
    if _HAVE_PKG_RESOURCES:
        return pkg_resources.resource_filename(_PACKAGE_NAME, _CACERT_NAME)
    else:
        mod = importlib.import_module(_PACKAGE_NAME)
        path = os.path.dirname(mod.__file__)
        return os.path.join(path, _CACERT_NAME)


def contents():
    if _HAVE_RESOURCE_READER:
        return importlib.resources.read_text(_PACKAGE_NAME, _CACERT_NAME, encoding="ascii")
    else:
        with open(where(), "r", encoding="ascii") as data:
            return data.read()
