/*
    53. Maximum Subarray [MEDIUM]
    
    Given an integer array nums, find the subarray
    with the largest sum, and return its sum.

    [KADANE'S ALGORITHM]
*/

#include <bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int>& nums) {
    int max = INT_MIN, sum = 0;

    for(int i=0; i<nums.size(); i++) {
        sum += nums[i];
        if(sum > max) max = sum;
        if(sum < 0) sum = 0;
    }

    return max;
}

// Follow Up: Print max subarray
void printMaxSubarray(vector<int>& nums) {
    int max = INT_MIN, sum = 0;
    int start = 0, ansStart = -1, ansEnd = -1; // extra

    for(int i=0; i<nums.size(); i++) {
        // everytime sum = 0 re-initialized => new subarray
        if(sum == 0) start = i;
        sum += nums[i];
        
        // max subarray found = update indices
        if(sum > max) {
            max = sum;
            ansStart = start;
            ansEnd = i;
        }

        if(sum < 0) sum = 0;
    }

    cout << "MAX SUBARRAY: [ ";
    for(int i=ansStart; i<ansEnd; i++)
        cout << nums[i] << " ";

    cout << "]" << endl;
}

int main() {
    int n;
    cout << "SIZE OF ARRAY: ";
    cin >> n;

    vector<int> arr(n);
    cout << "ARRAY: ";
    for(int i=0; i<arr.size(); i++)
        cin >> arr[i];

    printMaxSubarray(arr);
    cout << "MAX SUBARRAY SUM: " << maxSubArray(arr) << endl;
    return 0;
}