# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base cases
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        if not nums:
            return None

        # we get the middle
        middle = len(nums) // 2

        # we create a new node to serve as our root
        myNode = TreeNode(nums[middle], None, None)

        # we set the left node to be the center of the left subtree
        leftSubTree = nums[0:middle]
        myNode.left = self.sortedArrayToBST(leftSubTree)

        # we set the right node to be the center of the right subtree
        rightSubTree = nums[middle + 1:len(nums)]
        myNode.right = self.sortedArrayToBST(rightSubTree)

        return myNode