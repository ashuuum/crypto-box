import base64


def coding(target, encode):
    if encode:
        return base64.b64encode(target.encode('utf-8')).decode('utf-8')
    return base64.b64decode(target).decode('utf-8')