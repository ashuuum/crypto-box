import base64


def coding(target, encode):
    if encode:
        return base64.b16encode(target.encode('utf-8')).decode('utf-8')
    return base64.b16decode(target).decode('utf-8')