# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # helper function
    def helper(self, node, visited):
        # check if currently is a null None
        if node is None:
            return
        # go left
        self.helper(node.left, visited)
        # visit the node
        visited.append(node.val)
        # go right
        self.helper(node.right, visited)
        
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        visited = []
        
        self.helper(root, visited)
        return visited
