#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <sstream>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace std::chrono;

vector<unordered_set<string>> read_hypergraph(const string &filename) {
	vector<unordered_set<string>> hypergraph;
	ifstream file(filename);
	string line;
	
	if (file.is_open()) {
		while (getline(file, line)) {
			istringstream iss(line);
			unordered_set<string> edge;
			string vertex;
			while (iss >> vertex) {
				edge.insert(vertex);
			}
			hypergraph.push_back(edge);
		}
		file.close();
	}
	return hypergraph;
}

bool is_cover(const vector<unordered_set<string>> &hypergraph, const unordered_set<string> &vertex_cover) {
	for (const auto &edge : hypergraph) {
		bool covered = false;
		for (const auto &v : vertex_cover) {
			if (edge.find(v) != edge.end()) {
				covered = true;
				break;
			}
		}
		if (!covered) return false;
	}
	return true;
}

unordered_set<string> greedy_vertex_cover(const vector<unordered_set<string>> &hypergraph) {
	unordered_set<string> cover;
	vector<unordered_set<string>> edges = hypergraph;
	
	while (!edges.empty()) {
		unordered_map<string, int> vertex_count;
		for (const auto &edge : edges) {
			for (const auto &v : edge) {
				vertex_count[v]++;
			}
		}
		
		auto max_vertex_it = max_element(vertex_count.begin(), vertex_count.end(),
			[](const pair<string, int> &a, const pair<string, int> &b) {
				return a.second < b.second;
			});
		
		string v = max_vertex_it->first;
		cover.insert(v);
		
		vector<unordered_set<string>> new_edges;
		for (const auto &edge : edges) {
			if (edge.find(v) == edge.end()) {
				new_edges.push_back(edge);
			}
		}
		edges = new_edges;
	}
	return cover;
}

void save_vertex_cover(const string &filename, const unordered_set<string> &vertex_cover) {
	ofstream file(filename);
	if (file.is_open()) {
		for (const auto &v : vertex_cover) {
			file << v << " ";
		}
		file.close();
	}
}

int main() {
	string hypergraph_filename = "D:/CodeSpace/C++/AlgorithmsHomeWork/FinalAssignment/code/dataset_B/circuit_3.txt";
	string output_filename = "D:/CodeSpace/C++/AlgorithmsHomeWork/FinalAssignment/code/dataset_B/minimal_cover.txt";
	
	vector<unordered_set<string>> hypergraph = read_hypergraph(hypergraph_filename);
	
	auto start_time = high_resolution_clock::now();
	unordered_set<string> minimal_cover = greedy_vertex_cover(hypergraph);
	auto end_time = high_resolution_clock::now();
	auto duration = duration_cast<microseconds>(end_time - start_time);
	cout << "Time taken: " << duration.count() / 1000000.0 << " seconds" << endl;
	
	vector<string> sorted_cover(minimal_cover.begin(), minimal_cover.end());
	sort(sorted_cover.begin(), sorted_cover.end(), [](const string &a, const string &b) {
		return stoi(a) < stoi(b);
	});
	
	// Save minimal vertex cover to file
	save_vertex_cover(output_filename, unordered_set<string>(sorted_cover.begin(), sorted_cover.end()));
	
	cout << "Size of minimal vertex cover: " << minimal_cover.size() << endl;
	cout << "The minimal vertex cover is: ";
	for (const auto &v : sorted_cover) {
		cout << v << " ";
	}
	cout << endl;
	
	return 0;
}

