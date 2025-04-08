def caesar_encrypt(text, shift=3):
    cipher = ""
    for ch in text:
        if ch.isalpha():
            if ch.islower():
                cipher += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            else:
                cipher += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipher += ch
    return cipher

# === Main Logic ===
s = input("Enter a string to be encrypted: ")
encrypted = caesar_encrypt(s)
print(f"{encrypted} this is the cipher text")
