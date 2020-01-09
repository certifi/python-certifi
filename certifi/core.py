# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os


def where():

    # Overrides CA bundle location with custom value
    if os.environ.get('CERTIFI_CA_BUNDLE'):
        return os.environ.get('CERTIFI_CA_BUNDLE')

    f = os.path.dirname(__file__)

    return os.path.join(f, 'cacert.pem')
