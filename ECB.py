def encrypt_block(block, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(block)])

def decrypt_block(cipher_block, key):
    return encrypt_block(cipher_block, key)  # Symmetric for XOR

def ecb_encrypt(plaintext, key, block_size=8):
    ciphertext = bytearray()
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        if len(block) < block_size:
            block += bytes([0] * (block_size - len(block)))  # Padding
        encrypted = encrypt_block(block, key)
        ciphertext.extend(encrypted)
    return ciphertext

def ecb_decrypt(ciphertext, key, block_size=8):
    plaintext = bytearray()
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        decrypted = decrypt_block(block, key)
        plaintext.extend(decrypted)
    return plaintext

def bytes_to_hex(byte_data):
    return byte_data.hex()

def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

# === Main Execution ===
key = bytes([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6])  # 64-bit key

# Encrypt
input_text = input("Enter text to encrypt: ")
plaintext_bytes = input_text.encode()
cipher_bytes = ecb_encrypt(plaintext_bytes, key)
print("Encrypted (Hex):", bytes_to_hex(cipher_bytes))

# Decrypt
hex_input = input("Enter hex string to decrypt: ")
cipher_input = hex_to_bytes(hex_input)
decrypted = ecb_decrypt(cipher_input, key)
print("Decrypted Text:", decrypted.decode(errors="ignore"))  # ignore padding/nulls
