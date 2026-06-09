"""
169. Majority Element [Easy]

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.

You may assume that the majority element always exists in the array.
"""

# -------------------------------------------------------------------------------------------------------------------------


def majorityElement(nums):
    n = len(nums)

    if (n == 1) or (n == 2 and nums[0] == nums[1]):
        return nums[0]

    ctr = {}
    for num in nums:
        if num in ctr:
            ctr[num] += 1
            if ctr[num] > int(n / 2):
                return num
        else:
            ctr[num] = 1


if __name__ == "__main__":
    n = int(input("ARRAY LEN: "))
    arr = [int(x) for x in input("ARRAY: ").split(" ")]

    answer = majorityElement(arr)
    print(f"Majority Element in {arr} = {answer} ({arr.count(answer)} times)")
