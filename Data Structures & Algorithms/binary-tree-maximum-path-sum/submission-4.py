# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            max_path_at_node = max(0, left) + max(0, right) + node.val
            max_path = max(0, max(left, right)) + node.val
            res = max(res, max_path_at_node)

            return max_path
        dfs(root)
        return res