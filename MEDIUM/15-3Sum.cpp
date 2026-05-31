/*
    15. 3Sum [MEDIUM]

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
*/

#include <bits/stdc++.h>
using namespace std;

// Optimal approach = 3 pointer approach where
// i if fixed, j and k move based on the sum
// requires array to be sorted initially and no use of external set
vector<vector<int>> threeSum(vector<int> &nums)
{
    vector<vector<int>> ans;
    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size(); i++)
    {
        if (i > 0 && nums[i] == nums[i - 1])
            continue;

        int j = i + 1;
        int k = nums.size() - 1;

        while (j < k)
        {
            int sum = nums[i] + nums[j] + nums[k];

            // increment j to increase sum towards 0
            if (sum < 0)
                j++;

            // decrement k to decrease sum towards 0
            else if (sum > 0)
                k--;

            // sum = 0 => triplet found
            else
            {
                vector<int> temp = {nums[i], nums[j], nums[k]};
                ans.push_back(temp); // already sorted nums array

                // move j and k to next different number
                j++;
                k--;
                while (j < k && nums[j] == nums[j - 1])
                    j++;
                while (j < k && nums[k] == nums[k + 1])
                    k--;
            }
        }
    }

    return ans;
}

// // Better approach = run 2 loops for i and j and use
// // Hashing to find the 3rd element in the array, but should be careful
// // of the condition i != j != k

// /*
//     1 .Iterate over array using i and j
//     2. Calculate 3rd element using -(arr[i] + arr[j]).
//     3. Find 3rd element using hashset, if present, forms a triplet
//        and check for duplicate triplet if already present.
//     4. If element not found in hashet, increment j
//        and add previous element to hashset
//     5. Continue till j reaches end, then increment i, clear the hashset
//        and repeat from step 2 again till i = j = n-1
// */

// // Time complexity = O(n2 logM), M -> size of hashset
// // but Space complexity = O(n2) because external set being used
// vector<vector<int>> threeSum(vector<int> &nums)
// {
//     set<vector<int>> st;

//     for (int i = 0; i < nums.size(); i++) {
//         set<int> hashset; // start new hashset when 1 iteration done
//         for (int j = i + 1; j < nums.size(); j++) {
//             int third = -(nums[i] + nums[j]);

//             // hashset.find(ele) = end if ele not found
//             if(hashset.find(third) != hashset.end()) {
//                 vector<int> temp = { nums[i], nums[j], third };
//                 sort(temp.begin(), temp.end());
//                 st.insert(temp);
//             };

//             // add element to hashset when j increments
//             hashset.insert(nums[j]);
//         }
//     }

//     vector<vector<int>> ans(st.begin(), st.end());
//     return ans;
// }

// // Bruteforce approach = O(n3) ---------------------------------------
// vector<vector<int>> threeSum(vector<int> &nums)
// {
//     set<vector<int>> st;

//     for (int i = 0; i < nums.size(); i++)
//         for (int j = i + 1; j < nums.size(); j++)
//             for (int k = j + 1; k < nums.size(); k++)
//             {
//                 if (nums[i] + nums[j] + nums[k] == 0)
//                 {
//                     vector<int> temp = {nums[i], nums[j], nums[k]};
//                     sort(temp.begin(), temp.end());
//                     st.insert(temp);
//                 }
//             }

//     vector<vector<int>> ans(st.begin(), st.end());
//     return ans;
// }

int main()
{
    int len = 0;
    cout << "SIZE: ";
    cin >> len;

    vector<int> nums(len);
    cout << "ARRAY: ";
    for (int i = 0; i < len; i++)
        cin >> nums[i];

    vector<vector<int>> arr = threeSum(nums);
    cout << "3 Sum triplets: " << endl;
    for (int i = 0; i < arr.size(); i++)
    {
        cout << "Triplet " << i + 1 << ": ";
        for (int j = 0; j < arr[i].size(); j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }

    return 0;
}