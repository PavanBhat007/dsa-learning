"""
7. Reverse Integer [Medium]
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

# -------------------------------------------------------------------------------------------------------


def reverse(x: int) -> int:
  num = str(x)
  sign  = None #default
  if num[0] == '-':
    sign = num[0]

  output = 0
  if sign:
    output = (-1) * int(num[:0:-1])
    if output < (-1) * (2 ** 31):
      print("Reversed integer out of range!!")
      output = 0
  else:
    output = int(num[::-1])
    if output > (2 ** 31):
      print("Reversed integer out of range!!")
      output = 0

  return output


if __name__ == "__main__":
  num = int(input("NUM: "))
  print(f"Reverse of {num} = {reverse(num)}")