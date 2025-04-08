from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(plaintext.encode(), DES.block_size))).decode()

def decrypt(ciphertext_b64, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(ciphertext_b64)), DES.block_size).decode()

if __name__ == "__main__":
    key = input("Enter 8-byte key: ").encode()
    if len(key) == 8:
        plaintext = input("Enter plaintext: ")
        encrypted_text = encrypt(plaintext, key)
        print(f"Encrypted: {encrypted_text}")
        encrypted_text = input("Enter ciphertext to decrypt: ")
        key = input("Enter 8-byte key: to decode ").encode()
        if len(key) == 8:
            print(f"Decrypted: {decrypt(encrypted_text, key)}")
        else:
            print("Key must be exactly 8 bytes.")
    else:
        print("Key must be exactly 8 bytes.")
