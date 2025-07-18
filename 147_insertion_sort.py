# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # using bubble sort  
        if head is None:
            return None

        switched = True
        while switched:
            switched = False #  if there is sorted list then loop will run only n times
            current = head
            while current is not None and current.next is not None:
                if current.val > current.next.val:  #if x[j] > x[j+1] then swap x[j] with x[j+1]
                    switched = True # if there is need for sorting the list then this will run the next pass   
                    current.val,current.next.val = current.next.val ,current.val # if founded then swap both 
                current = current.next 
        return head # then return head