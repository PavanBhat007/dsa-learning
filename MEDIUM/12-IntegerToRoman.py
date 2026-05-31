"""
12. Integer to Roman [Medium]

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.
"""

# -----------------------------------------------------------------------------------------


def getSuitable(x: int, denom: list[int], index: int = 0) -> int:
  while x >= denom[index]:
      if index+1 >= len(denom):
          index += 1
          break
      index += 1
  return denom[index-1]


def intToRoman(num: int) -> str:
  numbers = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
  }

  denominations = list(numbers.keys())
  roman = ""
    
  while num:
    x = getSuitable(num, denominations)
    rem = num % x
    quo = num // x
            
    if quo > 1:
      roman += quo*numbers[x]

    elif rem == 0:
      try:
        roman += numbers[num]
      except KeyError:
        roman += num*numbers[x]
      break
    else:
      roman += numbers[x]
            
    num = rem

  return roman

if __name__ == "__main__":
  intInp = int(input("INT: ").strip())
  print(f"{intInp} -> {intToRoman(intInp)}")