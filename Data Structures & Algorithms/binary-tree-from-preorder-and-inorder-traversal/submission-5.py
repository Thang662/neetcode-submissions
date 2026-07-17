# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n2i_in = {inorder[i]: i for i in range(len(inorder))}
        pre_idx = 0

        def dfs(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left > right:
                return

            val = preorder[pre_idx]
            root = TreeNode(val)
            mid = n2i_in[val]
            pre_idx += 1

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            return root
        node = dfs(0, len(inorder) - 1)

        def print_tree(node: Optional[TreeNode]) -> None:
            if not node:
                return
            print_tree(node.left)
            print(node.val)
            print_tree(node.right)
        # node = tmp[preorder[0]]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.left.right = TreeNode(6)
        root.right = TreeNode(20)
        root.right.right = TreeNode(7)
        root.right.left = TreeNode(15)
        print_tree(node)
        
        return node