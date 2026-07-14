from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []

        while queue:
            tmp_res = None
            for i in range(len(queue)):
                node = queue.popleft()
                
                if node:
                    tmp_res = node.val
                    queue.append(node.left)
                    queue.append(node.right)
                
            if tmp_res is not None:
                res.append(tmp_res)

        return res