# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BFS 
        # (cur - p)(cur - q) <= 0 => cur is ancestor, else keep search!

        if not root:
            return root
        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if (cur.val - p.val)*(cur.val - q.val) <= 0:
                return cur
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        




