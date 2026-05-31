"""
58. Length of Last Word [Easy]

Given a string s consisting of words and spaces, 
return the length of the last word in the string.
"""

# ----------------------------------------------------------------------------------------------

def lengthOfLastWord(s: str) -> int:
  return len(s.strip().split(" ")[-1])

if __name__ == "__main__":
  string = input("STR: ")
  print(f"Length of last word in \"{string}\" is {lengthOfLastWord(string)}")