#include<iostream>
#include<string>
using namespace std;
int main()
{
    string a,b="";
    cout<<"Enter the String: ";
    cin>>a;
    for(int i=0;i<a.length();i++)
    {
        if(islower(a[i]))
        {
            b+=(char) (((int)a[i]+3 -'a')%26+'a');
        }
        else
        b+=(char) (((int)a[i]+3-'A')%26+'A');
    }    
    cout<<b;
    return 0;
}