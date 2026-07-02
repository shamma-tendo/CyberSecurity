def xor_cipher(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

secret = xor_cipher(b"Attack at dawn", b"mykey")
print(secret)
restored = xor_cipher(secret, b"mykey")
print(restored.decode())