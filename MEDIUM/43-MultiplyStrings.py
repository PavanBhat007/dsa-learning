"""
43. Multiply Strings [Medium]
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.
"""

#--------------------------------------------------------------------------------------------------


def multiply(n1, n2):
  return str( int(num1) * int(num2) )


if __name__ == "__main__":
  num1, num2 = input("NUMs:").strip().split(" ")
  print(f"{num1} * {num2} = {multiply(num1, num2)}")