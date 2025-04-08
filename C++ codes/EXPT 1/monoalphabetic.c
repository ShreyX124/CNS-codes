#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Function to encode text using Monoalphabetic Cipher
void monoalphabetic_cipher(char *text) {
    char substitution[26] = "ETAOINSHRDICUMWFGYPBVKJXQZ";
    for (int i = 0; text[i]; i++) {
        if (isalpha(text[i])) {
            char base = islower(text[i]) ? 'a' : 'A';
            text[i] = substitution[text[i] - base];
            if (islower(text[i])) text[i] = tolower(text[i]);
        }
    }
}

int main() {
    char text[100];
    printf("Enter text to encode using Monoalphabetic Cipher: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0'; // Remove newline character if present

    monoalphabetic_cipher(text);
    printf("Encoded Text: %s\n", text);
    return 0;
}
