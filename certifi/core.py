# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem or its contents.
"""


try:
    from .resources import where, read_text
except Exception:
    from .compat import where, read_text  # noqa: F401


def contents():
    return read_text("certifi", "cacert.pem")
