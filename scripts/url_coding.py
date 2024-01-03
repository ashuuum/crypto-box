import urllib.parse


def coding(target, encode):
    if encode:
        return urllib.parse.quote(target)
    return urllib.parse.unquote(target)