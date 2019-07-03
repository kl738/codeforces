#include <bits/stdc++.h>
using namespace std;

int main(){
    string myCard;
    cin >> myCard;
    char myR = myCard[0];
    char myS = myCard[1];
    int i = 0;
    string input;
    char r, s;
    bool flag = false;
    while(i < 5){
        cin >> input;
        r = input[0];
        s = input[1];
        if(myR == r || myS == s){
            flag = true;
        }
        i += 1;
    }
    if(flag == true){
        cout << "YES" << "\n";
    }
    else{
        cout << "NO" << "\n";
    }


        
}
