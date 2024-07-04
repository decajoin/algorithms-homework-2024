#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <sstream>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace std::chrono;

vector<unordered_set<int>> read_hypergraph(const string &filename) {
	vector<unordered_set<int>> hypergraph;
	ifstream file(filename);
	string line;

	if (file.is_open()) {
		while (getline(file, line)) {
			istringstream iss(line);
			unordered_set<int> edge;
			int vertex;
			while (iss >> vertex) {
				edge.insert(vertex);
			}
			hypergraph.push_back(edge);
		}
		file.close();
	}
	return hypergraph;
}

bool is_cover(const vector<unordered_set<int>> &hypergraph, const unordered_set<int> &vertex_cover) {
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

void find_minimal_covers(const vector<unordered_set<int>> &hypergraph, vector<unordered_set<int>> &minimal_covers) {
	vector<int> all_vertices;
	unordered_set<int> all_vertices_set;
	for (const auto &edge : hypergraph) {
		for (const auto &v : edge) {
			all_vertices_set.insert(v);
		}
	}
	all_vertices.assign(all_vertices_set.begin(), all_vertices_set.end());
	sort(all_vertices.begin(), all_vertices.end());

	function<void(int, unordered_set<int> &)> backtrack = [&](int index, unordered_set<int> &current_cover) {
		if (index == all_vertices.size()) {
			if (is_cover(hypergraph, current_cover)) {
				bool is_minimal = true;
				for (const auto &v : current_cover) {
					unordered_set<int> temp_cover = current_cover;
					temp_cover.erase(v);
					if (is_cover(hypergraph, temp_cover)) {
						is_minimal = false;
						break;
					}
				}
				if (is_minimal) {
					minimal_covers.push_back(current_cover);
				}
			}
			return;
		}

		int vertex = all_vertices[index];

		// 不包含当前顶点
		backtrack(index + 1, current_cover);

		// 包含当前顶点
		current_cover.insert(vertex);
		backtrack(index + 1, current_cover);
		current_cover.erase(vertex);
	};

	unordered_set<int> current_cover;
	backtrack(0, current_cover);
}

void save_vertex_cover(const string &filename, const unordered_set<int> &vertex_cover) {
	ofstream file(filename);
	if (file.is_open()) {
		vector<int> sorted_cover(vertex_cover.begin(), vertex_cover.end());
		sort(sorted_cover.begin(), sorted_cover.end());
		for (const auto &v : sorted_cover) {
			file << v << " ";
		}
		file.close();
	}
}

int main() {
	string hypergraph_filename = "D:/CodeSpace/C++/AlgorithmsHomeWork/FinalAssignment/code/dataset_B/min_25_20.txt";
	string output_filename = "D:/CodeSpace/C++/AlgorithmsHomeWork/FinalAssignment/code/dataset_B/minimal_cover.txt";

	vector<unordered_set<int>> hypergraph = read_hypergraph(hypergraph_filename);

	auto start_time = high_resolution_clock::now();
	vector<unordered_set<int>> minimal_covers;
	find_minimal_covers(hypergraph, minimal_covers);
	auto end_time = high_resolution_clock::now();
	auto duration = duration_cast<microseconds>(end_time - start_time);
	cout << "Time taken: " << duration.count() / 1000000.0 << " seconds" << endl;

	// 选择第一个极小顶点覆盖（或者可以选择最小的那个）
	unordered_set<int> minimal_cover = *min_element(minimal_covers.begin(), minimal_covers.end(), [](const unordered_set<int> &a, const unordered_set<int> &b) {
		return a.size() < b.size();
	});

	save_vertex_cover(output_filename, minimal_cover);

	cout << "Size of minimal vertex cover: " << minimal_cover.size() << endl;
	cout << "The minimal vertex cover is: ";
	vector<int> sorted_cover(minimal_cover.begin(), minimal_cover.end());
	sort(sorted_cover.begin(), sorted_cover.end());
	for (const auto &v : sorted_cover) {
		cout << v << " ";
	}
	cout << endl;

	return 0;
}

