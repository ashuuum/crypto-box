import hashlib


def crypto(target):
    return hashlib.sha1(target.encode().strip()).hexdigest()