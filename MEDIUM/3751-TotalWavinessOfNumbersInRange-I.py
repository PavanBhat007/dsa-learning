"""
3751. Total Waviness of Numbers in Range I [Medium]

You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:
- A digit is a peak if it is strictly greater than both of its immediate neighbors.
- A digit is a valley if it is strictly less than both of its immediate neighbors.
- The first and last digits of a number cannot be peaks or valleys.
- Any number with fewer than 3 digits has a waviness of 0.

Return the total sum of waviness for all numbers in the range [num1, num2].
"""

# -------------------------------------------------------------------------------------------------


def calculateWaninessOfSingleNumber(num):
    digits = [int(x) for x in str(num)]
    num_digits = len(digits)

    if num_digits < 3:
        return 0

    waviness = 0
    for i in range(num_digits):
        if i == 0 or i == num_digits - 1:
            continue

        prev, curr, next = digits[i - 1], digits[i], digits[i + 1]
        if (curr > prev and curr > next) or (curr < prev and curr < next):
            waviness += 1

    return waviness


def totalWavinessOfNumbersInRange(num1, num2):
    total_waviness = 0

    for num in range(num1, num2 + 1):
        total_waviness += calculateWaninessOfSingleNumber(num)

    return total_waviness


if __name__ == "__main__":
    range_start = int(input("RANGE START: "))
    range_end = int(input("RANGE END: "))

    answer = totalWavinessOfNumbersInRange(num1=range_start, num2=range_end)
    print(
        f"Total Waviness of numbers in the range [{range_start}, {range_end}] = {answer}"
    )
