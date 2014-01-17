Certifi: Python SSL Certificates
================================

This installable Python package contains a CA Bundle that you can reference
in your Python code. This is useful for verifying HTTP requests, for example.

This is the same CA Bundle which ships with the Requests codebase, and is
derived from Mozilla Firefox's cononical set.

Usage
-----

To reference the installed CA Bundle, you can use the built-in function::

    >>> import certifi

    >>> certifi.where()
    'certifi/cacert.pem'

Enjoy!