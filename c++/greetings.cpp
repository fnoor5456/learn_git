#include <iostream>

using namespace std;

int main(){
	cout << "Hello, what is your name?" << endl;
	string name;
	cin >> name;
	for(int i = 0; i < 10; i++)
		cout << "Hello " + name + "!";
}
