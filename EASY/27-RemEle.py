"""
27. Remove Element [Easy]

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

# ------------------------------------------------------------------------------------------------------------------

def removeElement(nums: list[int], val: int) -> list:
  i = 0
  limit = len(nums)
        
  while i != limit:
    if nums[i] == val:
      nums.pop(i)
      nums.append(val)
                
      limit -= 1
      if nums[i] == val:
        continue
      
    i += 1

  return nums[:i]


if __name__ == "__main__":
  arr = [int(x) for x  in input("ARR: ").strip().split(" ")]
  target = int(input("TARGET: ").strip())
  print(f"{arr} - {target} -> {removeElement(arr, target)}")