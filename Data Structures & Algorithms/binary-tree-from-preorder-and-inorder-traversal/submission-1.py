# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        # if root is same => l should be smaller than r
        def dfs(l,r):
            if l > r:
                return
            cur = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(cur)
            mid = indices[cur]
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(inorder) -1)