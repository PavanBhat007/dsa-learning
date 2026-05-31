"""
167. Two Sum II - Input Array Is Sorted [Medium]

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 

Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
"""

#-------------------------------------------------------------------------------------------------------------------------

def twoSumII(nums, target):
  start = 0
  end = len(nums)-1

  two_sum = nums[start] + nums[end]
  while two_sum != target:
    if two_sum < target and start+1 < end:
      start += 1
    elif two_sum > target and start < end-1:
      end -= 1
      
    two_sum = nums[start] + nums[end]
  
  return [start+1, end+1]
      
if __name__ == "__main__":
  nums = [-5,-4,-3,-2,-1]
  target = -8
  print(twoSumII(nums, target))