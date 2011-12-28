#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ceritfi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""

import os

_content = None


def where():
    f = os.path.split(__file__)[0]

    return os.path.join(f, 'cacert.pem')

def content():
    global _content

    if not _content:
        # global _content

        with open(where()) as f:
            _content = f.read()

    return _content


if __name__ == '__main__':
    print where()