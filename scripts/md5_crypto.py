import hashlib


def crypto(target):
    return hashlib.md5(target.encode().strip()).hexdigest()