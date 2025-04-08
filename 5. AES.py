from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# AES key must be 16, 24, or 32 bytes long
key = get_random_bytes(16)  # 128-bit AES key

# IV for CBC mode (always 16 bytes for AES)
iv = get_random_bytes(16)

# Your plaintext
plaintext = "This is a secret message."

# Encrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

# Encode ciphertext and IV for safe transmission/storage
ciphertext_b64 = base64.b64encode(ciphertext).decode()
iv_b64 = base64.b64encode(iv).decode()
key_b64 = base64.b64encode(key).decode()

# Decrypt
cipher_dec = AES.new(base64.b64decode(key_b64), AES.MODE_CBC, base64.b64decode(iv_b64))
decrypted = unpad(cipher_dec.decrypt(base64.b64decode(ciphertext_b64)), AES.block_size).decode()

# Output
print("Original:", plaintext)
print("Key (base64):", key_b64)
print("IV (base64):", iv_b64)
print("Encrypted (base64):", ciphertext_b64)
print("Decrypted:", decrypted)
