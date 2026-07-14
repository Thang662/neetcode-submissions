# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            is_good_node = 1 if node.val >= max_val else 0
            return is_good_node + dfs(node.left, max(max_val, node.val)) + dfs(node.right, max(max_val, node.val))
        
        return dfs(root, root.val)