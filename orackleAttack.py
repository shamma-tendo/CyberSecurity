from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class PaddingOracleServer:
    """Simulates a server that leaks padding validity - the vulnerability being demonstrated"""
    def __init__(self):
        self.key = os.urandom(16)

    def decrypt_and_check_padding(self, iv, ciphertext):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        
        pad_len = plaintext[-1]
        if pad_len < 1 or pad_len > 16:
            return False  # BAD PADDING (this leak is the vulnerability)
        if plaintext[-pad_len:] != bytes([pad_len] * pad_len):
            return False
        return True  # GOOD PADDING

print("This demonstrates why CBC mode without HMAC/AEAD is dangerous.")
print("Real fix: use AES-GCM or encrypt-then-MAC, and never leak padding validity to attackers.")