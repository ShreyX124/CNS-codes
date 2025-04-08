#include <iostream>
#include <unordered_set>
#include <cctype>  // For isalpha and tolower functions
using namespace std;

char replacer(char a[5][5], char z, bool encode = true) {
    if (!isalpha(z)) {
        return z;
    }

    z = tolower(z);
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (a[i][j] == z) {
                if (encode) {
                    return a[i][(j + 1) % 5];
                } else {
                    return a[i][(j +4) % 5];  // Shift column to the left for decoding
                }
            }
        }
    }
    return z; 
}

void matrix(char a[5][5], string key) {
    string alp = "abcdefghijklmnopqrstuvwxyz";
    unordered_set<char> exist;
    int i = 0, j = -1;

    for (char &c : key) {
        c = tolower(c);
    }

    for (char c : key) {
        if (exist.find(c) != exist.end()) continue;
        if (j == 4) {
            j = -1;
            i++;
        }
        if (i == 5) break;
        a[i][++j] = c;
        exist.insert(c);
    }

    for (char c : alp) {
        if (exist.find(c) != exist.end()) continue;
        if (j == 4) {
            j = -1;
            i++;
        }
        if (i == 5) break;
        a[i][++j] = c;
    }
}

string encode(char a[5][5], string s) {
    string e = "";
    for (char &c : s) {
        c = tolower(c);
        e += replacer(a, c, true);
    }
    cout << "Encoded string: " << e << endl;
    return e;
}

void decode(char a[5][5], string s) {
    string d = "";
    for (char &c : s) {
        c = tolower(c);
        d += replacer(a, c, false);
    }
    cout << "Decoded string: " << d << endl;
}

int main() {
    string key, str;
    cout << "Enter the string: ";
    getline(cin, str);
    cout << "Enter the key (no spaces): ";
    cin >> key;

    char a[5][5];
    matrix(a, key);

    cout << "Matrix:" << endl;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }

    string q=encode(a, str);
    decode(a, q);

    return 0;
}
