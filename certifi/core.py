#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os
import pkgutil
import tempfile
import warnings


class DeprecatedBundleWarning(DeprecationWarning):
    """
    The weak security bundle is being deprecated. Please bother your service
    provider to get them to stop using cross-signed roots.
    """


_certs_tempfile = None

def where():
    global _certs_tempfile
    if _certs_tempfile is not None:
        return _certs_tempfile.name

    f = os.path.dirname(__file__)
    cert_path = os.path.join(f, 'cacert.pem')
    if not os.path.exists(cert_path):
        # assume we are in a zip: attempt to extract to a temp file
        cert_data = pkgutil.get_data(__package__, 'cacert.pem')
        f = tempfile.NamedTemporaryFile(suffix='.pem')
        f.write(cert_data)
        f.flush()
        cert_path = f.name
        _certs_tempfile = f

    return cert_path


def old_where():
    warnings.warn(
        "The weak security bundle has been removed. certifi.old_where() is now an alias "
        "of certifi.where(). Please update your code to use certifi.where() instead. "
        "certifi.old_where() will be removed in 2018.",
        DeprecatedBundleWarning
    )
    return where()

if __name__ == '__main__':
    print(where())
