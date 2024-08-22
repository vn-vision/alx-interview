#!/usr/bin/python3
"""
Check whether a number is a valid UTF8
"""


def validUTF8(data):
    """
    Method determines if a given data is a valid UTF-8 encoding
    Each integer represents 1 byte of data, handle 8 least significant bits
    """

    encoded = []  # list to store data in binary '08b'
    _bool = []  # list to store bool based on validity

    for num in data:
        encoded.append(format(num, '08b'))

    # check the length of each encoded
    # if the length is past '08b': invalid

    for enc_num in encoded:
        if len(enc_num) > 8:
            _bool.append(False)
        else:
            _bool.append(True)

    # check which data has all valid utf-8
    if False in _bool:
        return False

    return True
