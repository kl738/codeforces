#include <bits/stdc++.h>
using namespace std;

int main(){
    int y,b,r;
    cin >> y >> b >> r;
    int yy = 1;
    int bb = 2;
    int rr = 3;
    int total = 6;
    while(yy<y && bb<b && rr<r){
        yy++;
        bb++;
        rr++;
        total += 3;
    }
    cout << total << "\n";
}