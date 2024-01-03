import codecs


def coding(target, encode):
    if encode:
        return codecs.encode(target, 'rot-13')
    return codecs.decode(target, 'rot-13')