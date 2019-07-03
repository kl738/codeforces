#include <bits/stdc++.h>
using namespace std;

int main(){
    int sw, sh;
    int w1, h1;
    int w2, h2;
    cin >> sw >> sh >> w1 >> h1 >> w2 >> h2;
    if(h1 > h2){
        while(sh >= h1){
            sw += sh;
            sh -= 1;
        }
        sw = max(0, sw-w1);
        while(sh >= h2){
            sw += sh;
            sh -= 1;
        }
        sw = max(0, sw-w2);
    }
    else{
        while(sh >= h2){
            sw += sh;
            sh -= 1;
        }
        sw = max(0, sw-w2);
        while(sh >= h1){
            sw += sh;
            sh -= 1;
        }
        sw = max(0, sw-w1);
    }

    while(sh > 0){
        sw += sh;
        sh -= 1;
    }


   

    cout << sw << "\n";
}