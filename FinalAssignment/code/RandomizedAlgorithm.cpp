#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>
#include <string>
#include <sstream>
#include <algorithm>
#include <chrono>
#include <random>

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

unordered_set<string> randomized_vertex_cover(const vector<unordered_set<string>> &hypergraph) {
	unordered_set<string> cover;
	vector<unordered_set<string>> edges = hypergraph;
	random_device rd;
	mt19937 gen(rd());
	
	while (!edges.empty()) {
		uniform_int_distribution<> edge_dist(0, edges.size() - 1);
		const auto &edge = edges[edge_dist(gen)];
		vector<string> edge_vertices(edge.begin(), edge.end());
		uniform_int_distribution<> vertex_dist(0, edge_vertices.size() - 1);
		string v = edge_vertices[vertex_dist(gen)];
		cover.insert(v);
		edges.erase(remove_if(edges.begin(), edges.end(), [&v](const unordered_set<string> &e) {
			return e.find(v) != e.end();
		}), edges.end());
	}
	return cover;
}

void save_vertex_cover(const string &filename, const unordered_set<string> &vertex_cover) {
	ofstream file(filename);
	if (file.is_open()) {
		vector<string> sorted_cover(vertex_cover.begin(), vertex_cover.end());
		sort(sorted_cover.begin(), sorted_cover.end(), [](const string &a, const string &b) {
			return stoi(a) < stoi(b);
		});
		for (const auto &v : sorted_cover) {
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
	unordered_set<string> minimal_cover = randomized_vertex_cover(hypergraph);
	auto end_time = high_resolution_clock::now();
	auto duration = duration_cast<microseconds>(end_time - start_time);
	cout << "Time taken: " << duration.count() / 1000000.0 << " seconds" << endl;
	
	save_vertex_cover(output_filename, minimal_cover);
	
	cout << "Size of minimal vertex cover: " << minimal_cover.size() << endl;
	cout << "The minimal vertex cover is: ";
	vector<string> sorted_cover(minimal_cover.begin(), minimal_cover.end());
	sort(sorted_cover.begin(), sorted_cover.end(), [](const string &a, const string &b) {
		return stoi(a) < stoi(b);
	});
	for (const auto &v : sorted_cover) {
		cout << v << " ";
	}
	cout << endl;
	
	return 0;
}

