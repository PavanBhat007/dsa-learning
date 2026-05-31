"""
26. Remove Duplicates from Sorted Array [Easy]

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, you need to do the following things:

Change the array nums such that the first k elements of nums 
contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

# -----------------------------------------------------------------------------------------------------

def removeDuplicates(nums: list[int]) -> list:
  i=1
  j=0
  while i < len(nums):
    if nums[j] == nums[i]:
      i += 1
    else:
      j += 1
      nums[j] = nums[i]

  return nums[:j+1]

if __name__ == "__main__":
  arr = [int(x) for x  in input("ARR: ").strip().split(" ")]
  print(f"{arr} -> {removeDuplicates(arr)}")