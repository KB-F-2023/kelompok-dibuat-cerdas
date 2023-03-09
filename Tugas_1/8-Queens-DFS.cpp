#include <iostream>
#include <vector>

using namespace std;

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

bool dfs(vector<int>& board, int row) {
    // Base case: If all queens are placed, return true
    if (row == 8) {
        return true;
    }

    // Try placing queen in each column of the current row
    for (int col = 0; col < 8; col++) {
        if (isSafe(board, row, col)) {
            board[row] = col; // Place the queen

            // Recur to place the rest of the queens
            if (dfs(board, row + 1)) {
                return true;
            }

            // If placing the queen in this column didn't work,
            // backtrack and try placing the queen in the next column
            board[row] = -1;
        }
    }

    return false; // If no solution is found, return false
}

void printSolution(vector<int>& board) {
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (board[i] == j) {
                cout << "Q ";
            } else {
                cout << ". ";
            }
        }
        cout << endl;
    }
    cout << endl;
}

int main() {
    vector<int> board(8, -1);

    if (dfs(board, 0)) {
        printSolution(board);
    } else {
        cout << "No solution found." << endl;
    }

    return 0;
}
