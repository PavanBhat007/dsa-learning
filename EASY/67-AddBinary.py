"""
67. Add Binary [Easy]

Given two binary strings a and b, 
return their sum as a binary string.
"""

# --------------------------------------------------------------------------

def binToDec(num: int) -> int:
  dec = 0
  for i in range(len(num)):
    dec += int(num[i]) * (2**i)
  return dec

def decToBin(num: int, binary: str) -> str:
  if num == 0:
    return binary
  binary += str((num%2))
  return decToBin(num//2, binary)

def addBinary(a: str, b: str) -> str:
  num1 = a[::-1]
  num2 = b[::-1]
  aDec = binToDec(num1)
  bDec = binToDec(num2)

  decSum = aDec + bDec
  if decSum == 0:
    return "0"
  else:
    binSum = decToBin(decSum, "")

  return binSum[::-1]

if __name__ == "__main__":
  n1, n2 = input("OPERANDS (a <space> b): ").strip().split(" ")
  sum = addBinary(n1, n2)
  print(f"{n1} [{binToDec(n1[::-1])}] +", 
        f"{n2} [{binToDec(n2[::-1])}] =",
        f"{sum} [{binToDec(sum[::-1])}]")
