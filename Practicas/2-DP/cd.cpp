#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// Versión sin dinámica
int mejor_cd(vector<int> const& canciones, int i, int k) {
	if (k < 0) return -2e5;
	if (i == canciones.size()) return 0;

	int c = canciones[i];
	return max(mejor_cd(canciones, i+1, k), mejor_cd(canciones, i+1, k-c)+c);
}

// Versión con dinámica
vector<vector<int>> mem;
int mejor_cd_din(vector<int> const& canciones, int i, int k) {
	if (k < 0) return -2e5;
	if (i == canciones.size()) return 0;

	if (mem[k][i] != -1) return mem[k][i];

	int c = canciones[i];
	return mem[k][i] = max(mejor_cd_din(canciones, i+1, k), mejor_cd_din(canciones, i+1, k-c)+c);
}

// El comando necesita ser llamado con un parámetro
// si se llama "./a.out b" resuelve sin dinámica
// si se llama "./a.out d" resuelve con dinámica
int main(int argc, char* argv[]) {
	if (argc != 2) return 1;

	// Primero se le escribe el peso máximo del CD, después la cantidad de canciones.
	int k, n;
	cin >> k >> n;

	// Después se le escribe el peso de cada canción
	vector<int> canciones(n);
	for (int j = 0; j < n; j++) cin >> canciones[j];

	if (*argv[1] == 'b')
		cout << mejor_cd(canciones, 0, k) << endl;

	if (*argv[1] == 'd') {
		mem = vector<vector<int>>(k+1, vector<int>(n+1, -1));
		cout << mejor_cd_din(canciones, 0, k) << endl;
	}
}
