def coding(target, encode):
    if encode:
        return '\\' + '\\'.join(hex(ord(char))[1:] for char in target)
    return bytes.fromhex(target.replace('\\x', '')).decode('utf-8')