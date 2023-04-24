def encode_rle(data):
    if not data:
        return b''
    encoded = bytearray()
    count = 1
    last_char = data[0]
    for i in range(1, len(data)):
        if data[i] == last_char:
            count += 1
        else:
            encoded.append(count)
            encoded.append(last_char)
            count = 1
            last_char = data[i]
    encoded.append(count)
    encoded.append(last_char)
    return bytes(encoded)

def decode_rle(data):
    if not data:
        return bytearray()
    decoded = bytearray()
    i = 0
    while i < len(data):
        if i + 1 < len(data):
            count = data[i]
            char = data[i + 1]
            decoded.extend([char] * count)
            i += 2
        else:
            break
    return bytes(decoded)

from hypothesis import given
from hypothesis.strategies import binary
import pytest

@given(binary())
def test_encode_decode_roundtrip(data):
    encoded = encode_rle(data)
    decoded = decode_rle(encoded)
    assert decoded == data

@given(binary())
def test_decode_encode_roundtrip(data):
    decoded = decode_rle(data)
    encoded = encode_rle(decoded)
    assert encoded == data

@given(binary())
def test_decode_length(data):
    decoded = decode_rle(data)
    assert len(decoded) % 2 == 0

@given(binary())
def test_encode_length(data):
    encoded = encode_rle(data)
    assert len(encoded) % 2 == 0