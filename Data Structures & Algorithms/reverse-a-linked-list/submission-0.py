# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        current = head
        while current:
            temp = current.next
            current.next = left
            #Update left and right
            left = current
            current = temp
        
        return left