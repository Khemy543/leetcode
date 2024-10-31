from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # find the midpoint of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # second part of the list is slow.next
        second = slow.next
        slow.next = None

        # reverse second part of the list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # prev contains the second part of the list
        # merge the two halfs of the list
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

