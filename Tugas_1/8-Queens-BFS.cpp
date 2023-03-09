#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct State {
    vector<int> board;
    int row;

    State(vector<int> b, int r) : board(b), row(r) {}
};

bool isSafe(vector<int>& board, int row, int col) {
    // Check if there is a queen in the same column
    for (int i = 0; i < row; i++) {
        if (board[i] == col)
            return false;
    }

    // Check if there is a queen in the diagonal to the left
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
        if (board[i] == j)
            return false;
    }

    // Check if there is a queen in the diagonal to the right
    for (int i = row - 1, j = col + 1; i >= 0 && j < 8; i--, j++) {
        if (board[i] == j)
            return false;
    }

    return true;
}

void bfs() {
    queue<State> q;

    // Add initial state to the queue
    vector<int> initial_board(8, -1);
    q.push(State(initial_board, 0));

    // BFS loop
    while (!q.empty()) {
        State current = q.front();
        q.pop();

        // Base case: If all queens are placed, print the board and return
        if (current.row == 8) {
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    if (current.board[i] == j)
                        cout << "Q ";
                    else
                        cout << "- ";
                }
                cout << endl;
            }
            return;
        }

        // Try placing queen in each column of the current row
        for (int col = 0; col < 8; col++) {
            if (isSafe(current.board, current.row, col)) {
                vector<int> new_board = current.board;
                new_board[current.row] = col; // Place the queen

                // Add the new state to the queue
                q.push(State(new_board, current.row + 1));
            }
        }
    }

    cout << "No solution found." << endl;
}

int main() {
    bfs();

    return 0;
}
