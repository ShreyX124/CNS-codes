def monoalphabetic_cipher(text):
    substitution = "ETAOINSHRDICUMWFGYPBVKJXQZ"
    result = ""

    for char in text:
        if char.isalpha():
            base = 'a' if char.islower() else 'A'
            index = ord(char.upper()) - ord('A')  # Get index in alphabet
            sub_char = substitution[index]
            result += sub_char.lower() if char.islower() else sub_char
        else:
            result += char  # Keep non-alphabetic characters as-is
    return result

# Input from user
text = input("Enter text to encode using Monoalphabetic Cipher: ")
encoded_text = monoalphabetic_cipher(text)
print("Encoded Text:", encoded_text)
