from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_message(public_key, message):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    return cipher_rsa.encrypt(message.encode())

def decrypt_message(private_key, ciphertext):
    private_key_obj = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key_obj)
    return cipher_rsa.decrypt(ciphertext).decode()

def main():
    private_key, public_key = generate_rsa_keys()
    print("\n🔑 Private Key:\n", private_key.decode())
    print("\n🔓 Public Key:\n", public_key.decode())
    message = input("\nEnter the message you want to encrypt: ")
    ciphertext = encrypt_message(public_key, message)
    print("\n🔐 Encrypted message:\n", ciphertext)
    decrypted_message = decrypt_message(private_key, ciphertext)
    print("\n📬 Decrypted message:\n", decrypted_message)

if __name__ == "__main__":
    main()
