def find_shift(plain_text, encrypted_text):
    for shift in range(26):
        decrypted = ""
        for ch in encrypted_text:
            if ch == " ":
                decrypted += " "
            elif ch.isupper():
                decrypted += chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A'))
            elif ch.islower():
                decrypted += chr((ord(ch) - ord('a') - shift + 26) % 26 + ord('a'))
            else:
                decrypted += ch
        if decrypted == plain_text:
            return shift
    return None

# === Main Execution ===
plain_text = input("Enter the plain text: ")
encrypted_text = input("Enter the encrypted text: ")

shift = find_shift(plain_text, encrypted_text)

if shift is not None:
    print(f"The correct Caesar shift is: {shift}")
else:
    print("No valid shift found that matches the encrypted text to the plain text.")
