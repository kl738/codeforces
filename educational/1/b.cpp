#include <iostream>
#include <string>
using namespace std;

int main(){
	string s;
	int m;
	int l, r, k;
	int length;
	int net;
 	cin >> s; 
	cin >> m;
	for(int i = 0; i < m; ++i){
		cin >> l >> r >> k;
		length = r - l + 1;
		net = k % length;
		if(net == 0) net = length;
		rotate(s.begin() + l-1, s.begin() + r-net, s.begin() + r);		
	}
	cout << s << "\n";
}
