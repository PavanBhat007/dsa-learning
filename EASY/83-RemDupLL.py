"""
83. Remove Duplicates from Sorted List [Easy]

Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
"""

# --------------------------------------------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
      return f"{self.val} -> {self.next}"

def deleteDuplicates(head):
    if head == None:
      return None

    prev = head
    curr = head.next

    while curr != None:
      if prev.val != curr.val:
        prev = curr
        curr = curr.next
      else:
        prev.next = curr.next
        curr = curr.next


    return head
  
  
def getLinkedList(numList):
  head = ListNode(val=int(numList[0]))
  prev_node = head
  
  for num in numList[1:]:
    new_node = ListNode(val=int(num))
    new_node.next = None
    prev_node.next = new_node
    prev_node = new_node
    
  return head   
  

def main(l):
  ll = getLinkedList(l)
  
  result = deleteDuplicates(ll)
  print(result)
    

if __name__ == "__main__":
  l = input("LIST: ").strip().split(" ")
  main(l)