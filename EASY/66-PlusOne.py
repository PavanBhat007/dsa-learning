"""
66. Plus One [Easy]

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

# ----------------------------------------------------------------------------------------------

def plusOne(digits: list[int]) -> list[int]:
  return [ int(y) for y in str(int("".join([str(x) for x in digits])) + 1) ]

if __name__ == "__main__":
  num = [int(x) for x in input("NUM: ").strip()]
  print(f"{num} + 1 = {plusOne(num)}")