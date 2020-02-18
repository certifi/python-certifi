# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import importlib.resources
import os


def where():
    f = os.path.dirname(__file__)

    return os.path.join(f, 'cacert.pem')


def what():
    with importlib.resources.open_binary("certifi", "cacert.pem") as fh:
        return fh.read()
