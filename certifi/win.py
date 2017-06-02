#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
from ctypes import wintypes
import os

import wincertstore

"""
win.py
~~~~~~~~~~

This module copies the local store certificates to the current cacert.pem
file and caches it localy.
"""

# Create ctypes wrapper for Win32 functions we need, with correct argument/return types
_CreateMutex = ctypes.windll.kernel32.CreateMutexA
_CreateMutex.argtypes = [wintypes.LPCVOID, wintypes.BOOL, wintypes.LPCSTR]
_CreateMutex.restype = wintypes.HANDLE

_WaitForSingleObject = ctypes.windll.kernel32.WaitForSingleObject
_WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
_WaitForSingleObject.restype = wintypes.DWORD

_ReleaseMutex = ctypes.windll.kernel32.ReleaseMutex
_ReleaseMutex.argtypes = [wintypes.HANDLE]
_ReleaseMutex.restype = wintypes.BOOL

_CloseHandle = ctypes.windll.kernel32.CloseHandle
_CloseHandle.argtypes = [wintypes.HANDLE]
_CloseHandle.restype = wintypes.BOOL

INFINITE = 0xFFFFFFFF


PEM_PATH = os.path.join(os.environ['APPDATA'], '.certifi', 'cacert.pem')


def where():
    return PEM_PATH


def get_pems(store_names=None):
    store_names = store_names or ("CA", "ROOT")
    for store_name in store_names:
        with wincertstore.CertSystemStore(store_name) as store:
            for cert in store.itercerts(usage=wincertstore.SERVER_AUTH):
                try:
                    pem_entry = '# Label: "{name}"\n{pem}'.format(
                        name=cert.get_name(),
                        pem=cert.get_pem().decode('ascii')
                    )
                except UnicodeEncodeError:
                    pem_entry = ''

                yield pem_entry


handle = _CreateMutex(None, False, 'Global_certifi')
_WaitForSingleObject(handle, INFINITE)

if not os.path.exists(PEM_PATH):
    os.makedirs(os.path.dirname(PEM_PATH))

with open(PEM_PATH, 'w') as f:

    local_pem = os.path.join(os.path.split(__file__)[0], 'cacert.pem')
    with open(local_pem) as lf:
        f.write(lf.read())

    for pem in get_pems():
        f.write(pem)

_ReleaseMutex(handle)
_CloseHandle(handle)


if __name__ == '__main__':
    print(PEM_PATH)
