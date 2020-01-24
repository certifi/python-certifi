# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os


def where():

    if 'PYTHON_CERTIFI_WHERE' in os.environ:
        return os.environ['PYTHON_CERTIFI_WHERE']

    f = os.path.dirname(__file__)

    return os.path.join(f, 'cacert.pem')
