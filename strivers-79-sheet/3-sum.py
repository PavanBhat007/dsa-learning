"""
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets in the array that sum to zero.
    
    Approach:
    1. Sort the array → helps in skipping duplicates and using two-pointer technique
    2. Fix the first element (i), then use two pointers (left & right) to find pair
       that sums to -nums[i]
    3. Skip duplicates for i, left, and right to avoid duplicate triplets
    """
    if len(nums) < 3:
        return []
    
    nums.sort()  # crucial step
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # Now find two numbers after i that sum to -nums[i]
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                    
                # Skip duplicates for right
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif current_sum < 0:
                # Sum too small → need larger numbers → move left pointer right
                left += 1
            else:
                # Sum too big → need smaller numbers → move right pointer left
                right -= 1
    
    return result


if __name__ == "__main__":
    test_cases = [
        [-1, 0, 1, 2, -1, -4],          # classic case
        [0, 1, 1],                      # no triplet
        [0, 0, 0, 0],                   # multiple zeros
        [-2, -2, 0, 0, 2, 2],           # duplicates
        []                              # empty
    ]
    
    for nums in test_cases:
        print(f"Input: {nums}")
        triplets = threeSum(nums)
        print("Triplets:")
        for t in triplets:
            print("   ", t)
        print()