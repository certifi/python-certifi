#!/usr/bin/env python
import os
import sys

import setuptools

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()

if __name__ == '__main__':
    setuptools.setup()
