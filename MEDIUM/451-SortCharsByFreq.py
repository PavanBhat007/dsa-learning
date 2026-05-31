"""
451. Sort Characters By Frequency [Medium]

Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
"""

# ------------------------------------------------------------------------------------

def frequencySort(s: str) -> str:
  freqMap = {}

  for char in s:
    if char in freqMap:
        freqMap[char] += 1
    else:
      freqMap[char] = 1
        
  sortedMap = {k: v for k, v in sorted(freqMap.items(), 
      key=lambda item: item[1], 
      reverse=True)}
        
  return ("".join([ k*v for k, v in sortedMap.items()]))

if __name__ == "__main__":
  word = input("WORD: ").strip()
  print(f"{word} sorted using character frequency: {frequencySort(word)}")