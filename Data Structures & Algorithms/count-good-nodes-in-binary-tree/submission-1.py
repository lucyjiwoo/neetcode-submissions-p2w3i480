# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, m, gn_count):
            if not root:
                return 
            if root.val >= m:
                gn.append(root)
                m = root.val
            dfs(root.left, m, gn)
            dfs(root.right, m, gn)
        m = root.val
        gn = []
        dfs(root, m, gn)
        return len(gn)

