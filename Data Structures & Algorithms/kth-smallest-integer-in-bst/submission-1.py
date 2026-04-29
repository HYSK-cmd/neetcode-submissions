# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None
        def inorderDFS(node):
            if not node or self.ans is not None:
                return
            inorderDFS(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            #res.append(node.val)
            inorderDFS(node.right)
        inorderDFS(root)
        return self.ans
        
