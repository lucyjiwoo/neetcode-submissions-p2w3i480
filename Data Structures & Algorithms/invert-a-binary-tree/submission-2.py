# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left and root.right:
                l,r = root.left, root.right
                root.left = self.invertTree(r)
                root.right = self.invertTree(l)
            elif root.left:
                l = root.left
                root.left = None
                root.right = self.invertTree(l)
            elif root.right:
                r = root.right
                root.right = None
                root.left = self.invertTree(r)
            else:
                return root
        return root