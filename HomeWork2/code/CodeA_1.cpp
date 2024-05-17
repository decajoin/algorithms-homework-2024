#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ifstream file("./dataset_a/Number_2e5.txt");
    if (!file.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    vector<long long> numbers;
    long long num;
    while (file >> num) {
        numbers.push_back(num);
    }
    file.close();

    sort(numbers.begin(), numbers.end());

    cout << "Smallest numbers: " << endl;
    for (int i = 0; i < 10; ++i) {
        cout << numbers[i] << endl;
    }

    return 0;
}