# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Remember this is Linked list
        trash = ListNode()
        current = trash
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            
            Sum = val1 + val2 + carry
            carry = Sum // 10
            sum_node = ListNode(Sum % 10)
            current.next = sum_node

            current = current.next if current else None    
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return trash.next
    
    
'''
Exmaple for l1 = 2,4,4 and l2 = 5,6,3
 1 itreation :- Sum = 2 + 5 + 0 = 7
            : carry = 7 // 10 = 0
            : sum_node = ListNode(Sum % 10) # 7 % 10 = 7
            : current.next = sum_node
            : current = current.next
 2 itreation :- Sum = 6 + 4 + 0 = 10
             : carry = 10 // 10 = 1
             : sum_node = ListNode(10 % 10) = 1
             : current.next = sum_node
             : current = current.next
3 itreation :- Sum = 4 + 3 + 1 = 8
             : carry = 8 // 10 = 0
             : sum_node = ListNode(sum_node % 10)
             : current.next = sum_node
             :current = current.next
    * so we have value in our trash node [0,7,0,8] 
    * we return from 1 So {return trash.next}
'''