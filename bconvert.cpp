#include <iostream>
using namespace std;

//vector<char> numbers[36][1] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
string numbers = "0123456789abcdefghijklmnopqrstuvwxyz";

string bconv(string num, int sbase, int fbase) {
	//converting to base 10
	unsigned long long ten = std::stoull(num, nullptr, sbase);
	//converting to end base
	string answer = "";
	while (ten != 0) {
		int remain = ten % fbase;
		answer = numbers[remain] + answer;
		ten = (ten - remain) / fbase;
	}
	return answer;
}

int main(void) {
	int sbase = 0, fbase = 0;
	string n = "-";
	bool negative = false;
	cout << "What would you like to convert?\n";
	getline(cin, n);
	if (n.at(0) == '-') {
		negative = true;
		n = n.substr(1);
	}
	while (not (sbase <= 36 and sbase >= 2)) {
		cout << "\nWhat base is this in?\n";
		cin >> sbase;
	}
	while (not (fbase <= 36 and fbase >= 2)) {
		cout << "\nWhat base are you converting this number to?\n";
		cin >> fbase;
	}
	string answer = bconv(n, sbase, fbase);
	if (negative) {
		answer = "-" + answer;
	}
	cout << "\n" << answer;
} 
