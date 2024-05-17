#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <algorithm>

using namespace std;

int random_partition(vector<long long>& nums, int left, int right) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(left, right);
    int pivotIndex = dis(gen);
    
    long long pivot = nums[pivotIndex];
    swap(nums[pivotIndex], nums[right]);

    int i = left;
    for (int j = left; j < right; j++) {
        if (nums[j] < pivot) {
            swap(nums[i], nums[j]);
            i++;
        }
    }

    swap(nums[i], nums[right]);
    return i;
}

long long quick_select(vector<long long>& nums, int left, int right, int k) {
    if (left == right) {
        return nums[left];
    }

    int pivotIndex = random_partition(nums, left, right);
    
    if (k == pivotIndex) {
        return nums[k];
    } else if (k < pivotIndex) {
        return quick_select(nums, left, pivotIndex - 1, k);
    } else {
        return quick_select(nums, pivotIndex + 1, right, k);
    }
}

vector<long long> find_smallest_numbers(vector<long long>& nums) {
    int n = nums.size();
    if (n <= 10) {
        sort(nums.begin(), nums.end());
        return nums;
    } else {
        vector<long long> smallestNumbers;
        for (int i = 0; i < 10; i++) {
            long long num = quick_select(nums, 0, n - 1, i);
            smallestNumbers.push_back(num);
        }
        return smallestNumbers;
    }
}

int main() {
    string filename = "./dataset_a/Number_2e5.txt";
    ifstream inputFile(filename);

    if (!inputFile) {
        cerr << "Failed to open file: " << filename << endl;
        return 1;
    }

    vector<long long> M;
    long long num;
    while (inputFile >> num) {
        M.push_back(num);
    }

    inputFile.close();

    vector<long long> smallestNumbers = find_smallest_numbers(M);

    cout << "Smallest numbers: " << endl;
    for (long long num : smallestNumbers) {
        cout << num << endl;
    }

    return 0;
}