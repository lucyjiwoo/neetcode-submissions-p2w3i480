# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(rootp, rootq):
            if not rootq:
                if not rootp:
                    return True
            if rootp and rootq and rootp.val == rootq.val:
                if dfs(rootp.left,rootq.left) and dfs(rootp.right,rootq.right):
                    return True
                else:
                    return False
            else:
                return False
        return dfs(p,q)

        