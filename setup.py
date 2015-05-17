#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import sys

from setuptools import setup

version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('certifi/__init__.py', 'r') as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        VERSION = match.group(1)
    else:
        raise RuntimeError("No version number found!")

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()

required = []
setup(
    name='certifi',
    version=VERSION,
    description='Python package for providing Mozilla\'s CA Bundle.',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='http://certifi.io/',
    packages=[
        'certifi',
    ],
    package_dir={'certifi': 'certifi'},
    package_data={'certifi': ['*.pem']},
    # data_files=[('certifi', ['certifi/cacert.pem'])],
    include_package_data=True,
    license='ISC',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
)
