/*
    118. Pascal's Triangle [EASY]
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it.
*/

#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> generate(int numRows) {
    vector<vector<int>> pT {{1}};
    vector<int> prev = pT[0];

    // row=1 becuase the initial [1] is the first row (row 0)
    for (int row=1; row < numRows; row++) {
        // for each row ...
        vector<int> temp {1}; // new temp for each row

        // append all the summations of previous row
        if(prev.size() != 1) {
            // i and j are adjacent pointers that sum up the prev array
            for(int i=0, j=i+1; j<prev.size(); i++, j++) {
                temp.push_back(prev[i] + prev[j]);
            }
        }

        temp.push_back(1);
        pT.push_back(temp);
        prev = temp;
    }

    return pT;
}

int main() {
    int rows;
    cout << "ROWS: ";
    cin >> rows;

    vector<vector<int>> pascalsTriangle = generate(rows);

    for(int i=0; i<pascalsTriangle.size(); i++) {
        for(int j=0; j<pascalsTriangle[i].size(); j++)
            cout << pascalsTriangle[i][j] << " ";
        cout << endl;
    }

    return 0;
}