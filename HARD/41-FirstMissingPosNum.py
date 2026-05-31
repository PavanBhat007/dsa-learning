"""
41. First Missing Positive [Hard]
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""

#----------------------------------------------------------------------------------------------


def firstMissingPositive(nums):
  nums.append(0)
  n = len(nums)

  for i in range(len(nums)):
    if nums[i]<0 or nums[i]>=n:
      nums[i] = 0


  for i in range(len(nums)):
    nums[nums[i]%n] += n
      

  for i in range(1,len(nums)):
    if nums[i]//n==0:
      return i
          
  return n 
         
if __name__ == "__main__":
  nums = [int(x) for x in input("NUMS: ").strip().split(" ")]
  print(f"Missing number: {firstMissingPositive(nums)}")