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


_cert_tempfile = None
_cert_path = os.path.join(os.path.dirname(__file__), 'cacert.pem')
try:
    if not os.path.exists(_cert_path):
        # assume we are in a zip: attempt to extract to a temp file
        cert_data = pkgutil.get_data(__package__, 'cacert.pem')
        if cert_data is not None:
            _cert_tempfile = tempfile.NamedTemporaryFile(suffix='.pem')
            _cert_tempfile.write(cert_data)
            _cert_tempfile.flush()
            _cert_path = _cert_tempfile.name
except Exception as e:
    # preserve previous behaviour: If any exception occurs, just warn about it
    warnings.warn('cacert.pem not found; exception raised trying to create it: ' + str(e))


def where():
    return _cert_path


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
