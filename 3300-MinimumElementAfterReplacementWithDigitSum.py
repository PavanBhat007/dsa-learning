"""
3300. Minimum Element After Replacement With Digit Sum [Easy]

You are given an integer array nums. You replace each element in nums with the sum of its digits.
Return the minimum element in nums after all replacements.
"""

# -------------------------------------------------------------------------------------------------------------------------


def sumOfDigits(num):
    sum = 0
    while num != 0:
        lastDigit = num % 10
        sum += lastDigit
        num = int(num / 10)

    return sum


def minimumElementAfterReplacementWithDigitSum(nums):
    minEle = sumOfDigits(nums[0])
    for num in nums[1:]:
        digitSum = sumOfDigits(num)
        if digitSum <= minEle:
            minEle = digitSum

    return minEle


if __name__ == "__main__":
    n = int(input("ARRAY LEN: "))
    arr = [int(x) for x in input("ARRAY: ").split(" ")]

    print(
        f"Minimum Element after Repacement with Digit Sum: {minimumElementAfterReplacementWithDigitSum(arr)}"
    )
