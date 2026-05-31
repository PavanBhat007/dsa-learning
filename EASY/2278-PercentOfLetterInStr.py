"""
2278. Percentage of Letter in String [Easy]

Given a string s and a character letter, 
return the percentage of characters in s that equal letter 
rounded down to the nearest whole percent.
"""

# -------------------------------------------------------------------------------------------------

def percentageLetter(s: str, letter: str) -> int:
  return int((s.count(letter)/len(s))*100)

if __name__ == "__main__":
  string = input("STR: ").strip()
  letter = input("LETTER: ").strip()
  print(f"Percentage of letter \"{letter}\" in \"{string}\" {percentageLetter(string, letter)}")