# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root, level, res):
            if not root:
                return 
            
            if len(res) <= level:
                res.append([])
            res[level].append(root.val)
            bfs(root.left,level+1,res)
            bfs(root.right,level+1,res)
        res = []
        bfs(root, 0, res)
        return res
            