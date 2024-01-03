import hashlib


def crypto(target):
    return hashlib.sha256(target.encode().strip()).hexdigest()