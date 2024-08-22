#!/usr/bin/python3
"""
Check whether a number is a valid UTF8i
valid utf-encoding follows the pattern for each byte 1 - 4
    4 - 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
    3 - 1110xxxx 10xxxxxx 10xxxxxx
    2 - 110xxxxx 10xxxxxx
    1 - 0x00 to 0x7F
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
        if len(enc_num) == 32:
            # 4 byte character
            if enc_num[0:5] == '11110' and \
                    enc_num[8:10] == enc_num[16:18] == enc_num[24:26] == '10':
                _bool.append(True)
            else:
                _bool.append(False)

        elif len(enc_num) == 24:
            # 3 byte character
            if enc_num[0:5] == '1110' and \
                    enc_num[8:10] == enc_num[16:18] == '10':
                _bool.append(True)
            else:
                _bool.append(False)

        elif len(enc_num) == 16:
            # 2 byte character
            if enc_num[0:5] == '110' and enc_num[8:10] == '10':
                _bool.append(True)
            else:
                _bool.append(False)

        elif len(enc_num) <= 8:
            # 1 byte character
            _bool.append(True)
        else:
            # other formats
            _bool.append(False)

    # check which data has all valid utf-8
    if False in _bool:
        return False

    return True
