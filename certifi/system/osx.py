import os
import subprocess


SYSTEM_KEYCHAIN = '/Library/Keychains/System.keychain'
SYSTEM_CA_KEYCHAIN = '/System/Library/Keychains/SystemRootCertificates.keychain'
USER_CA_BUNDLE = os.path.expanduser('~/Library/Caches/certifi/OS-bundle.pem')


def mtime_or_never(filename):
    try:
        mtime = os.stat(filename).st_mtime
        return mtime
    except OSError:
        return float('-inf')


def try_security():
    try:
        return subprocess.check_output(['security', 'find-certificate', '-a', '-p'])
    except subprocess.CalledProcessError:
        # Assume that nothing is wrong and set this to blank
        return ''


if not os.path.exists(USER_CA_BUNDLE):
    OS_TRUSTED_CERTS = try_security()
else:
    max_time = max(mtime_or_never(SYSTEM_KEYCHAIN), mtime_or_never(SYSTEM_CA_KEYCHAIN))
    if max_time > mtime_or_never(USER_CA_BUNDLE):
        OS_TRUSTED_CERTS = try_security()
    else:
        OS_TRUSTED_CERTS = ''
