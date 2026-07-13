# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return True, 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            is_balance = left[0] and right[0] and (abs(left[1] - right[1]) < 2)
            height = max(left[1], right[1])
            return is_balance, 1 + height

        res = dfs(root)
        return res[0]