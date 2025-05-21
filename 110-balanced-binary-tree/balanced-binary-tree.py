# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]) -> int :
        if root is None :
            return 0
        else:
            lsh = self.height(root.left)
            rsh = self.height(root.right)
            return max(lsh,rsh) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
       
        curr_left = root.left
        curr_right = root.right

        l,r = self.height(curr_left) , self.height(curr_right)
        
        if abs(l-r) > 1 :
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)


