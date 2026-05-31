"""
28. Find the Index of the First Occurrence in a String [Easy]
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""

# --------------------------------------------------------------------------------

def strStr(haystack: str, needle: str) -> int:
  if needle in haystack:
    return haystack.index(needle)
  else:
    return -1
       
if __name__ == "__main__":
  h, n = input("HAYSTACK  NEEDLE: ").strip().split(" ")
  index = strStr(h, n)
  if index != -1:
    print(f"{n} found in {h} at position {index+1}")
  else:
    print(f"{n} not found in {h}")