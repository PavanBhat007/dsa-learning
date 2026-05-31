"""
35. Search Insert Position [Easy]
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
"""

# --------------------------------------------------------------------------------

def searchInsert(nums: list[int], target: int) -> int:
  for i in range(len(nums)):
    ele = nums[i]
    if target <= ele:
      return i
        
  if nums[-1] <= target:
    return len(nums)
  

if __name__ == "__main__":
  arr = [int(x) for x in input("ARR: ").strip().split(" ")]
  val = int(input("VAL: "))
  ind = searchInsert(arr, val)
  print(f"{arr[:ind]} - {val} - {arr[ind:]}")