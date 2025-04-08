def substitution_encrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower()  # Ensure the key is in lowercase
    
    if len(key) != 26 or len(set(key)) != 26:
        raise ValueError("Key must be a string of 26 unique letters.")

    cipher = ""
    
    for ch in text:
        if ch.isalpha():
            # Convert letter to lowercase for mapping
            is_upper = ch.isupper()
            ch = ch.lower()
            
            # Find the corresponding letter in the key
            index = alphabet.index(ch)
            encrypted_char = key[index]
            
            # If the original letter was uppercase, convert the encrypted letter to uppercase
            if is_upper:
                encrypted_char = encrypted_char.upper()
            
            cipher += encrypted_char
        else:
            # If not a letter, leave the character unchanged
            cipher += ch
    
    return cipher

# === Main Logic ===
s = input("Enter a string to be encrypted: ")
key = input("Enter a 26-letter substitution key (using all letters of the alphabet): ")

try:
    encrypted = substitution_encrypt(s, key)
    print(f"Encrypted text: {encrypted}")
except ValueError as e:
    print(e)
