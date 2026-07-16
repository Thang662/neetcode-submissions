# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, count = None, 0
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal res, count
            if not node: return
            dfs(node.left)
            if count == k:
                return
            count += 1
            if count == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
        