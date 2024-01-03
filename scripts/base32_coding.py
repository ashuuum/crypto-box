import base64


def coding(target, encode):
    if encode:
        return base64.b32encode(target.encode('utf-8')).decode('utf-8')
    return base64.b32decode(target).decode('utf-8')