"""
2. Add Two Numbers [Medium]

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
"""

#-------------------------------------------------------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
      return f"{self.val} -> {self.next}"



def addTwoNumbers(l1, l2):
  # linked list nums being reversed helps us here since we need to add from the right
  # keep adding node.val of l1 to node.val of l2 until either one of then hits a node.next = None
  # then just append the remaining nodes of the other linked list to result
  
  result = []
  lhs = l1
  rhs = l2
  carry = 0

  
  while True:
    if (lhs != None) and (rhs != None):
      digit_sum = lhs.val + rhs.val + carry
      
      if digit_sum >= 10:
        result.append(digit_sum%10)
        carry = (digit_sum // 10)%10
      else:
        result.append(digit_sum)
        carry = 0
        
      lhs = lhs.next
      rhs = rhs.next
      
    elif lhs == None:
      while rhs != None:
        tmp_sum = rhs.val + carry
        
        if tmp_sum >= 10:
            result.append(tmp_sum%10)
            carry = (tmp_sum // 10)%10
        else:
          result.append(tmp_sum)
          carry = 0
        
        rhs = rhs.next
        
      if carry:
        result.append(carry)
        
      break
        
        
    elif rhs == None:
      while lhs != None:
        tmp_sum = lhs.val + carry
        
        if tmp_sum >= 10:
            result.append(tmp_sum%10)
            carry = (tmp_sum // 10)%10
        else:
          result.append(tmp_sum)
          carry = 0
        
        lhs = lhs.next
      
      if carry:
        result.append(carry)
        
      break
        
    else:
      break
    
  return getLinkedList(result)



def getLinkedList(numList):
  head = ListNode(val=int(numList[0]))
  prev_node = head
  
  for num in numList[1:]:
    new_node = ListNode(val=int(num))
    new_node.next = None
    prev_node.next = new_node
    prev_node = new_node
    
  return head
    
  

def main(l1 ,l2):
  ll1 = getLinkedList(l1)
  ll2 = getLinkedList(l2)
  
  result = addTwoNumbers(ll1, ll2)
  print(result)
  
  tmp = []
  ptr = result
  while ptr != None:
    tmp.append(str(ptr.val))
    ptr = ptr.next
    
  print(f"{''.join(reversed(l1))} + {''.join(reversed(l2))} = {''.join(reversed(tmp))}")

if __name__ == "__main__":
  num1 = input("Number 1: ").strip().split(" ")
  num2 = input("Number 2: ").strip().split(" ")
  main(num1, num2)