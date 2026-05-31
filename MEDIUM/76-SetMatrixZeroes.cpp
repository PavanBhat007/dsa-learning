/*
    73. Set Matrix Zeroes [MEDIUM]
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
*/

#include <bits/stdc++.h>
using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    vector<bool> zeroRows(rows, false);
    vector<bool> zeroCols(cols, false);

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            if (matrix[i][j] == 0) {
                zeroRows[i] = true;
                zeroCols[j] = true;
            }

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            if (zeroRows[i] || zeroCols[j])
                matrix[i][j] = 0;
}

int main() {
    int rows, cols;
    cin >> rows >> cols;

    vector<vector<int>> matrix(rows, vector<int>(cols));
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cin >> matrix[i][j];
        }
    }

    setZeroes(matrix);

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
