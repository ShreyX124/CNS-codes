def encrypt_caesar(text, shift):
    result = ""
    for ch in text:
        if ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += ch
    return result

def decrypt_all_shifts(cipher_text, original_text):
    for i in range(26):
        decrypted = ""
        for ch in cipher_text:
            if ch == " ":
                decrypted += " "
            elif ch.isupper():
                decrypted += chr((ord(ch) - ord('A') - i + 26) % 26 + ord('A'))
            elif ch.islower():
                decrypted += chr((ord(ch) - ord('a') - i + 26) % 26 + ord('a'))
            else:
                decrypted += ch
        print(f"Shift {i}: {decrypted}")
        if decrypted == original_text:
            print(f"Correct shift is: {i}")
            return
    print("Correct shift not found")

# === Main Execution ===
original_text = input("Enter the plain text: ")
shift = int(input("Enter the desired shift: "))

encrypted_text = encrypt_caesar(original_text, shift)
print("Encrypted text:", encrypted_text)

decrypt_all_shifts(encrypted_text, original_text)
