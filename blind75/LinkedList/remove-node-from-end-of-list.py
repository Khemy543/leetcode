from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy to add a new node to begining of list
        dummy = ListNode(0, head)

        # left is the begining of the dummy node
        left = dummy
        right = head
        
        # right is starts from the nth node
        while n > 0 and right:
            right = right.next
            n -= 1

        # move both pointers by one unitl right is none
        while right:
            left = left.next
            right = right.next
        
        # delete the node that is in front of the node left points to
        left.next = left.next.next

        return dummy.next