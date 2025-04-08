#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, c = "";
    cout << "Enter a string to be encrypted: ";
    getline(cin, s);
    for (int i = 0; i < s.length(); i++) {
        char ch = s[i];
        if (isalpha(ch)) {
            c += islower(ch) ? (char)(((ch - 'a' + 3) % 26) + 'a') : (char)(((ch - 'A' + 3) % 26) + 'A');
        } else {
            c += ch; 
        }
    }
    cout << c << " this is the cipher text";
    return 0;
}
