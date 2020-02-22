#include <iostream>
#include <cmath>
#include <string>
using namespace std;

string factor(int number) {
	int factors[2][100], pointer = 0;
	double inn = number;
	for (int j = 2; j < sqrt(inn); j++) {
		if (inn / j == std::floor(inn / j)) {
			inn = inn / j;
			int power = 1;
			while (inn / j == std::floor(inn / j)) {
				inn = inn / j;
				power = power + 1;
			}
			factors[0][pointer] = j;
			factors[1][pointer] = power;
			pointer = pointer + 1;
		}
	}
	factors[0][pointer] = inn;
	factors[1][pointer] = 1;
	pointer++;
	string answer;
	for (int f = 0; f < pointer; ++f) {
		answer = answer + to_string(factors[0][f]) + " ^ " + to_string(factors[1][f]) + ", ";
	}
	return answer;
}	

int main() {
	double number;
	cout << "What would you like to factor?\n";
	cin >> number;
	string factors = factor(number);
	cout << factors;
	cout << "Done!";
}
	
