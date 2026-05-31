"""
1752. Check if Array Is Sorted and Rotated [Easy]

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero).
Otherwise, return false. There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.
"""

# -------------------------------------------------------------------------------------------------


def checkArraySortedAndRotated(nums):
    n = len(nums)
    if n == 1:
        return True

    dip_index = 0
    second_dip = False

    for i in range(1, n):
        if not nums[i] >= nums[i - 1]:
            if dip_index == 0:
                dip_index = i
            else:
                second_dip = True
                break
    
    if dip_index == 0:
        return True
    elif second_dip:
        return False
    else:
        for i in range(dip_index, n):
            if not nums[i] <= nums[0]:
                return False

        return True


if __name__ == "__main__":
    n = int(input("ARRAY LEN: "))
    arr = [int(x) for x in input("ARRAY: ").strip().split(" ")]

    answer = checkArraySortedAndRotated(arr)
    if answer:
        print("Array was sorted and reversed")
    else:
        print("Array was not sorted or rotated")
