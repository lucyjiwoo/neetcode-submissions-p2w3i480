# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergelist(self, list1, list2):
        res, cur = None, None
        cur1, cur2 = list1, list2
        if not cur1:
            return list2
        elif not cur2:
            return list1
        while cur1 and cur2:
            if not res:
                if cur1.val <= cur2.val:
                    res = ListNode(cur1.val)
                    cur1 = cur1.next
                else:
                    res = ListNode(cur2.val)
                    cur2 = cur2.next
                cur = res
            else:
                if cur1.val <= cur2.val:
                    cur.next = ListNode(cur1.val)
                    cur1 = cur1.next
                else:
                    cur.next = ListNode(cur2.val)
                    cur2 = cur2.next
                cur = cur.next
        if cur1:
            cur.next = cur1
        elif cur2:
            cur.next = cur2
        return res
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists:
            res = lists[0]
        else:
            return None
        for i in range(1,len(lists)):
            res = self.mergelist(res if res else None,lists[i])
        return res
        
        