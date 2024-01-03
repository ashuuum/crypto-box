import hashlib


def crypto(target):
    return hashlib.sha512(target.encode().strip()).hexdigest()