from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# DES key must be exactly 8 bytes
key = b'8bytekey'

# Message to encrypt
plaintext = "HelloWorld"  # any string

# Create cipher
cipher = DES.new(key, DES.MODE_ECB)

# Padding plaintext to be multiple of 8 bytes
padded_text = pad(plaintext.encode(), DES.block_size)

# Encrypt
ciphertext = cipher.encrypt(padded_text)
ciphertext_b64 = base64.b64encode(ciphertext).decode()

# Decrypt
decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), DES.block_size).decode()

# Output
print("Original:", plaintext)
print("Encrypted (base64):", ciphertext_b64)
print("Decrypted:", decrypted)
