import os as _os
from os import path as _path
import sys as _sys


if _sys.platform == 'darwin':
    from . import osx
    OS_TRUSTED_CERTS = osx.OS_TRUSTED_CERTS
    CA_BUNDLE = osx.USER_CA_BUNDLE
else:
    # Unsupported platform for this feature
    OS_TRUSTED_CERTS = ''
    CA_BUNDLE = None


def _regenerate_where():
    certifi_pem = _path.abspath(_path.join(_path.split(__file__)[0], '..', 'cacert.pem'))
    if not CA_BUNDLE:
        return certifi_pem
    elif OS_TRUSTED_CERTS:
        if not _path.exists(_path.dirname(CA_BUNDLE)):
            _os.makedirs(_path.dirname(CA_BUNDLE))
        with open(CA_BUNDLE, 'wb') as user_bundle:
            with open(certifi_pem, 'rb') as built_in_pem:
                certifi_certs = built_in_pem.read()
            user_bundle.write(certifi_certs + '\n' + OS_TRUSTED_CERTS)
        return CA_BUNDLE
    else:
        return CA_BUNDLE


WHERE = _regenerate_where()


__all__ = ('WHERE',)
