"""
20. Valid Parentheses [Easy]

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

# ----------------------------------------------------------------------------------------------------------------------------------

class ValidParantheses:
    def __init__(self):
        self.stack = []

    def push(self, x: int):
        self.stack.append(x)

    def pop(self) -> str:
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isValid(self, s: str) -> bool:
        for bracket in s:
            if bracket in ['(', '{', '['] and len(s) !=0:
                self.push(bracket)

            if bracket in [')', '}', ']'] and (len(s) == 1 or len(self.stack) == 0):
                return False

            if (bracket == ')' and ('(' not in self.stack)) \
            or (bracket == ']' and ('[' not in self.stack)) \
            or (bracket == '}' and ('{' not in self.stack)):
                return False

            topEle = self.peek()
            if (bracket == ')' and topEle == '(') \
            or (bracket == ']' and topEle == '[') \
            or (bracket == '}' and topEle == '{'):
                self.pop()

        if len(self.stack) == 0:
            return True
        else:
            return False
          
if __name__ == "__main__":
  sol = ValidParantheses()
  string = input(" STR: ")
  if sol.isValid(string):
    print(f"\"{string}\" is VALID")
  else:
    print(f"\"{string}\" is INVALID")
            