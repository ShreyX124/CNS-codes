#include <iostream>
#include <unordered_set>
#include <cctype>  // For isalpha and tolower functions
using namespace std;

char replacer(char a[5][5], char z) {
    // If the character is not an alphabet, return it unchanged
    if (!isalpha(z)) {
        return z;
    }

    // Convert character to lowercase to handle case-insensitive encoding
    z = tolower(z);

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (a[i][j] == z) {
                return a[i][(j + 1) % 5]; // Shift column to the right
            }
        }
    }
    return z; // Return unchanged if not in the matrix (although this shouldn't happen)
}

void matrix(char a[5][5], string key) {
    string alp = "abcdefghijklmnopqrstuvwxyz";
    unordered_set<char> exist;
    int i = 0, j = -1;

    // Convert the key to lowercase and remove non-alphabetic characters
    for (char &c : key) {
        c = tolower(c);
    }

    // Fill matrix with key
    for (char c : key) {
        if (exist.find(c) != exist.end()) continue; // Skip duplicates
        if (j == 4) {
            j = -1;
            i++;
        }
        if (i == 5) break; // Matrix full
        a[i][++j] = c;
        exist.insert(c);
    }

    // Fill remaining alphabet
    for (char c : alp) {
        if (exist.find(c) != exist.end()) continue; // Skip if already in key
        if (j == 4) {
            j = -1;
            i++;
        }
        if (i == 5) break; // Matrix full
        a[i][++j] = c;
    }
}

void encode(char a[5][5], string s) {
    string e = "";
    // Convert input string to lowercase and process each character
    for (char &c : s) {
        c = tolower(c); // Ensure case insensitivity
        e += replacer(a, c); // Replace each character
    }
    cout << "Encoded string: " << e << endl;
}

int main() {
    string key, str;
    cout << "Enter the string: ";
    getline(cin, str);
    cout << "Enter the key (no spaces): ";
    cin >> key;

    // Initialize and create the matrix
    char a[5][5];
    matrix(a, key);

    // Print the matrix (optional, for debugging)
    cout << "Matrix:" << endl;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }

    // Encode the string
    encode(a, str);

    return 0;
}