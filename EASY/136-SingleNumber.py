"""
136. Single Number [Easy]

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

#-------------------------------------------------------------------------------------------------------------------------

def singleNonRepeatingNumber(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    # using a stack based appraoch with sorted array
    # when number appears first time, push
    # and if number already in stack (2nd time), pop from stack
    # only the single non-repeating number will remain in the stack at the end
    stack = []  # 1D array can be used without violating "constant extra space"
    nums.sort() # takes linear time so won't the condition "linear runtime complexity"

    for num in nums:
        if num in stack:
            stack.pop() # repeating nums will be together because of sorting
        else:
            stack.append(num)
        
    return stack[0]

if __name__ == "__main__":
    n = int(input("ARRAY LEN: "))
    arr = [int(x) for x in input("ARRAY: ").split(" ")]

    answer = singleNonRepeatingNumber(arr)
    print(f"The single non-repeating number in array {arr} is {answer}")
