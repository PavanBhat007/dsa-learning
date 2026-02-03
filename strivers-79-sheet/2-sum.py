"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
"""

"""
--- BRUTE-FORCE ALGORITHM (2-pointer approach) ---
for i = 0 --> n:
  for j = i+1 --> n:
    if nums[i] + nums[j] == target:
      return (i,j)

This is a O(n^2) solution because of the 2 nested for loops.

--- BEST SOLUTION (HashMap based solution) ---
map = {} -> key=element, value=index
for i = 0 --> n:
  complement = target - nums[i] // this gives the required 2nd number
  if (map.has(complement))      // if we already encountered this 2nd num
    return (map.get(complement), i)

  map.set(nums[i], i) // set each ele:idx in map for future lookup
"""

def two_sum(nums, target):
  map = {} # initialize empty map

  for i in range(len(nums)):
      complement = target - nums[i] # 2nd num required
      if complement in list(map.keys()): # 2nd num in map??
          return [map[complement], i]
            
      map[nums[i]] = i # add other elements to map sequentially
            
  return [-1, -1] # when no elements sum = target in nums


if __name__ == "__main__":
  n = int(input("SIZE: "))
  arr = [int(x) for x in input("ARRAY: ").strip().split(" ")]
  target = int(input("TARGET: "))

  result = two_sum(arr, target)
  print(result)