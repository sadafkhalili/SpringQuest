#include <iostream>
#include <stack>
#include <random>
using namespace std;

pair<int, int> start = {1, 1};
pair<int, int> finish;
const int MAX_N = 1000;
int plane[MAX_N][MAX_N];
bool savevisited[MAX_N][MAX_N];
int n;

pair<int, int> spring = {-1, -1};
int springSteps;
int side;
pair<int, int> path[MAX_N * MAX_N];
int length = 0;

int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1};

int randomInt(int min, int MAX_N) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(min, MAX_N);
    return dis(gen);
}

void generateplane() {
    finish.first = randomInt(1, n);
    finish.second = randomInt(1, n);

    int p = randomInt(1, n);
    for (int i = 0; i < p; i++) {
        int x = randomInt(1, n);
        int y = randomInt(1, n);
        if ((x != start.first || y != start.second) && (x != finish.first || y != finish.second)) {
            plane[x][y] = -1;
        }
    }

    if (randomInt(1, 100) <= 30) {
        spring = {randomInt(1, n), randomInt(1, n)};
        springSteps = randomInt(1, n / 2);
        side = randomInt(0, 7);
        if (spring != start && spring != finish) {
            plane[spring.first][spring.second] = 4;
        }
    }

    pair<int, int> tunnel = {randomInt(1, n), randomInt(1, n)};
    if (tunnel != start && tunnel != finish) {
        plane[tunnel.first][tunnel.second] = 5;
    }
}

bool isValid(int x, int y) {
    return x >= 1 && x <= n && y >= 1 && y <= n && plane[x][y] != -1 && !savevisited[x][y];
}

bool findPath() {
    stack<pair<int, int>> s;
    s.push(start);

    while (!s.empty()) {
        auto [x, y] = s.top();
        s.pop();

        path[length++] = {x, y};

        if (x == finish.first && y == finish.second) {
            return true;
        }

        savevisited[x][y] = true;

        if (spring.first == x && spring.second == y) {
            for (int i = 0; i < springSteps; i++) {
                x += dx[side];
                y += dy[side];
                if (!isValid(x, y)) break;
            }
        }

        if (plane[x][y] == 5) {
            for (int i = 0; i < 3; i++) {
                if (length > 0) length--;
            }
            if (length > 0) {
                x = path[length - 1].first;
                y = path[length - 1].second;
            }
        }

        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (isValid(nx, ny)) {
                s.push({nx, ny});
            }
        }
    }

    return false;
}

void printplane() {
    cout << "plane: " << endl;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == start.first && j == start.second)
                cout << "S";
            else if (i == finish.first && j == finish.second)
                cout << "G";
            else if (plane[i][j] == 4)
                cout << "F";
            else if (plane[i][j] == 5)
                cout << "T";
            else
                cout << "*";
        }
        cout << endl;
    }
}

void printPath() {
    cout << " [";
    for (int i = 0; i < length; ++i) {
        cout << "(" << path[i].first << ", " << path[i].second << ")";
        if (i != length - 1) cout << " --> ";
    }
    cout << "]" << endl;
}

int main() {
    cout << "Enter n: ";
    cin >> n;
    if (n < 6) {
        cout << "It must be at least 6." << endl;
        return 0;
    }

    generateplane();
    printplane();

    if (findPath()) {
        cout << "Path Found!" << endl;
        printPath();
    }
}

