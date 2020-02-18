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
    return importlib.resources.read_text("certifi", "cacert.pem")
