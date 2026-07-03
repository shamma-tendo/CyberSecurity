import os

def generate_key(length):
    return os.urandom(length)

def otp_encrypt(message: bytes, key: bytes) -> bytes:
    return bytes(m ^ k for m, k in zip(message, key))

message = b"TOP SECRET"
key = generate_key(len(message))
ciphertext = otp_encrypt(message, key)
decrypted = otp_encrypt(ciphertext, key)  # XOR again to decrypt

print("Cipher:", ciphertext)
print("Decrypted:", decrypted.decode())