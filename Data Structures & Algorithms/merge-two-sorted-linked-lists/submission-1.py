# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        tail = None
        head = None
        if not p1:
            return list2
        elif not p2:
            return list1
        while p1 and p2:
            if p1.val <= p2.val:
                if tail:
                    tail.next = p1
                    tail = tail.next
                else:
                    tail = p1
                    head = p1
                p1 = p1.next
            else:
                if tail:
                    tail.next = p2
                    tail = tail.next
                else:
                    tail = p2
                    head = p2
                p2 = p2.next
        if p1:
            tail.next = p1
        elif p2:
            tail.next = p2
        return head
