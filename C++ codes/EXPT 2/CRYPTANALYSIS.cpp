#include<iostream>
using namespace std;
int main()
{
    //caeser cypher brute force cryptanalysis
    string s;
    cout<<"Enter the plain text: ";
    getline(cin,s);
    string q=s;
    cout<<"Enter the desired shift: ";
    int shift;
    cin>>shift;
    for(int i=0;i<s.length();i++)
    {
        if(s[i]>='a' && s[i]<='z')
        {
            s[i]=char((int(s[i]-'a')+shift)%26+'a');
        }
        else if(s[i]>='A' && s[i]<='Z')
        {
            s[i]=char((int(s[i]-'A')+shift)%26+'A');
        }
    }
    cout<<"Encrypted text: "<<s<<endl;
    for(int i=0;i<26;i++)
    {
        cout<<"Shift "<<i<<": ";
        string b;
        for(int j=0;j<s.length();j++)
        {
            if(s[j]==' ')
            {
                cout<<" ";
                continue;
            }
            if(isupper(s[j]))
            {
                b+=char(int(s[j]-65-i+26)%26+65);
                cout<<char(int(s[j]-65-i+26)%26+65);
            }
            else
            {
                b+=char(int(s[j]-97-i+26)%26+97);
                cout<<char(int(s[j]-97-i+26)%26+97);
            }
        }
        cout<<endl;
        if(b==q)
        {
            cout<<"Shift is: "<<i<<endl;
            return 0;
        }
    }
    cout<<"Shift not found"<<endl;
    return 0;
}