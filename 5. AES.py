from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

# Function to encrypt data
def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)  # Using CBC mode for AES encryption
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))  # Pad data before encryption
    return cipher.iv + ciphertext  # Return IV concatenated with ciphertext

# Function to decrypt data
def aes_decrypt(encrypted_data, key):
    iv = encrypted_data[:16]  # Extract the IV (first 16 bytes)
    ciphertext = encrypted_data[16:]  # Extract the ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Reinitialize cipher with the same key and IV
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Unpad the decrypted data
    return decrypted_data.decode()

# Main function to allow custom input for encryption and decryption
def main():
    key = get_random_bytes(16)  # AES key (16 bytes = 128-bit key)
    print(f"Using key: {binascii.hexlify(key).decode()}")  # Print key in hex (for reference)

    # Encrypt data
    data = input("Enter the string to encrypt: ")  # Input data to encrypt
    encrypted_data = aes_encrypt(data, key)
    print("Encrypted:", binascii.hexlify(encrypted_data).decode())  # Show the encrypted data in hex

    # Decrypt data
    encrypted_input = input("Enter the encrypted string to decrypt (in hex): ")  # Input encrypted data in hex
    encrypted_data = binascii.unhexlify(encrypted_input)  # Convert hex back to bytes
    decrypted_data = aes_decrypt(encrypted_data, key)  # Decrypt the data
    print("Decrypted:", decrypted_data)  # Show decrypted data

if __name__ == "__main__":
    main()
