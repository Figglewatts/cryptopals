#!/usr/bin/env python

# cryptopals.py
# functions for cryptopals

BASE64_ALPHABET = \
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="


def base64encode(byte_arr):
    """
    Encodes an array of binary values to a base64 string.
    Args:
        byte_arr - the array of bytes to encode
    Returns:
        A base64 encoding of the given binary data
    """
    length = len(byte_arr)
    paddingAmount = length % 3
    base64_string = ""

    # blocks of 3 bytes
    for i in range(0, len(byte_arr), 3):
        if i + 3 > len(byte_arr):
            base64_string += BASE64_ALPHABET[64] * paddingAmount
            break
        fullbits = (byte_arr[i] << 16) + (byte_arr[i+1] << 8) + byte_arr[i+2]
        base64_chars = [
            BASE64_ALPHABET[fullbits >> 18],
            BASE64_ALPHABET[(fullbits >> 12) & 63],
            BASE64_ALPHABET[(fullbits >> 6) & 63],
            BASE64_ALPHABET[fullbits & 63]
        ]
        base64_string += ''.join(base64_chars)
    return base64_string
