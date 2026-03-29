# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = root
        if temp:
            if root.left and root.right:
                l,r = temp.left, temp.right
                root.left = self.invertTree(r)
                root.right = self.invertTree(l)
            elif root.left:
                l = temp.left
                root.left = None
                root.right = self.invertTree(l)
            elif temp.right:
                r = temp.right
                root.right = None
                root.left = self.invertTree(r)
            else:
                return root
        return root