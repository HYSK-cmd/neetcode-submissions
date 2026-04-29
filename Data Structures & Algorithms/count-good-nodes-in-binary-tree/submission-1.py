# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.good = 0
        def dfs(self, node, max_so_far):
            if node.val >= max_so_far:
                self.good += 1
                max_so_far = node.val
            if node.left:
                dfs(self, node.left, max_so_far)
            if node.right:
                dfs(self, node.right, max_so_far)
        dfs(self, root, root.val)
        return self.good