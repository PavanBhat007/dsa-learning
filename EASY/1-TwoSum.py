"""
1. Two Sum [EASY]
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

#------------------------------------------------------------------------------------------------------------------------

def twoSum(nums, target):
  for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
      
if __name__ == "__main__":
  nums = [-1,-2,-3,-4,-5]
  target = -8
  print(twoSum(nums, target))