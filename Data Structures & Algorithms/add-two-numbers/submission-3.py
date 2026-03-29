# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1,l2
        ex = (cur1.val + cur2.val)//10
        new_head = ListNode((cur1.val + cur2.val)%10)
        cur = new_head
        cur1 = cur1.next
        cur2 = cur2.next
        while cur1 and cur2:
            v = (cur1.val + cur2.val + ex)%10
            ex = (cur1.val + cur2.val + ex)//10
            cur.next = ListNode(v)
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next

        if not cur2:
            while cur1:
                v = (cur1.val + ex)%10
                ex = (cur1.val + ex)//10
                cur.next = ListNode(v)
                cur = cur.next
                cur1 = cur1.next
        if not cur1:
            while cur2:
                v = (cur2.val + ex)%10
                ex = (cur2.val + ex)//10
                cur.next = ListNode(v)
                cur = cur.next
                cur2 = cur2.next
        if ex > 0:
            cur.next = ListNode(ex)
        return new_head
            





        