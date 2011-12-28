#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


from distutils.core import setup



if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

required = []
setup(
    name='certifi',
    version='0.0.3',
    description='Mozilla\'s SSL Certs.',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='http://python-requests.org',
    packages=[
        'certifi',
    ],
    # package_dir={'mypkg': 'src/mypkg'},
    # data_files=[('certifi', ['cacert.pem'])],
    # package_data = {'certifi'}
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
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
)
