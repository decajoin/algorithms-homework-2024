#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <chrono>   

using namespace std;
using namespace std::chrono;

vector<vector<int>> findEquivalentClasses(const vector<string>& strings) {
    unordered_map<string, vector<int>> hashTable;

    // 构建哈希表
    for (int i = 0; i < strings.size(); ++i) {
        hashTable[strings[i]].push_back(i); 
    }

    // 等价类划分
    vector<vector<int>> equivalentClasses;
    for (const auto& entry : hashTable) {
        equivalentClasses.push_back(entry.second);
    }

    return equivalentClasses;
}


int main() {

    string filename = "./dataset/Letter.txt";

    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error: Unable to open file!" << endl;
        return 1;
    }

    // 读取文件并存储到 vector<string> 中
    vector<string> data;
    string line;
    while (getline(file, line)) {
        // 删除行末的换行符
        if (!line.empty() && line[line.size() - 1] == '\r') {
            line.erase(line.size() - 1);
        }
        // 将每一行的元素间隔的Tab替换为""
        for(int i=0;i<line.size();i++)
        {
            if(line[i]=='\t')
            {
                line.erase(i,1);
            }
        }
        data.push_back(line);
    }

    // 记录算法开始时间
    auto start = high_resolution_clock::now();

    vector<vector<int>> equivalentClasses = findEquivalentClasses(data);

    // 记录算法结束时间
    auto stop = high_resolution_clock::now();

    // 计算算法执行时间（毫秒）
    auto duration = duration_cast<milliseconds>(stop - start);

    // 输出执行时间
    cout << "对 " << filename << " 进行等价类划分，算法执行时间: " << duration.count() << " 毫秒" << endl;

    // 输出等价类划分结果
    for (const auto& classIndices : equivalentClasses) {
        for (int index : classIndices) {
            cout << index + 1 << " ";
        }
        cout << endl;
    }

    // 关闭文件
    file.close();

    return 0;
}
