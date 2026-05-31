"""
9. Palindrome Number [EASY]
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

#-----------------------------------------------------------------------------------------------------------------------

def isPalindrome(x: int) -> bool:
  return str(x) == str(x)[::-1]

if __name__ == "__main__":
  num = input("NUMBER: ")
  
  if isPalindrome(num):
    print(f"{num} is a PALINDROME")
  else:
    print(f"{num} is NOT A PALINDROME")
    