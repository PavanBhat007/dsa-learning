"""
154. Find Minimum in Rotated Sorted Array II [Hard]

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 

For example, the array nums = [0,1,4,4,5,6,7] might become:
- [4,5,6,7,0,1,4] if it was rotated 4 times.
- [0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array. 
You must decrease the overall operation steps as much as possible.
"""

# -------------------------------------------------------------------------------------------------------------------------

def minimumInRotatedSortedArray(nums):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return min(nums[0], nums[1])
    else:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
            
    return nums[0]
            
if __name__ == "__main__":
    n = int(input("ARRAY LEN: "))
    arr = [int(x) for x in input("ARRAY: ").split(" ")]

    answer = minimumInRotatedSortedArray(arr)
    print(f"Minimum element is sorted rotated array {arr} is {answer}")