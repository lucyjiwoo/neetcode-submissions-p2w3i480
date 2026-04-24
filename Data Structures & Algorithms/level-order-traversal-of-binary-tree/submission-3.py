# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(0,root)])
        if not root:
            return []
        res, prev = [], 0
        nodes = []
        while queue:            
            level, node = queue.popleft()
            if prev != level:
                res.append(nodes)
                prev = level
                nodes = []
            nodes.append(node.val)
            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1, node.right))
        res.append(nodes)
        return res


