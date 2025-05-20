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
            lh = self.height(root.left)
            rh = self.height(root.right)
            return max(lh,rh) + 1  
    def NodesAtKdist(self, root: Optional[TreeNode], k) -> List[int]:
        if root is None:
            return
        if k == 0:
            return [root.val]
        left_sub = self.NodesAtKdist(root.left,k-1)
        right_sub = self.NodesAtKdist(root.right,k-1)
        if left_sub is None:
            return right_sub
        if right_sub is None:
            return left_sub
        if right_sub is None and left_sub is None:
            return 
        else:
            return left_sub + right_sub
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = self.height(root)
        res = []
        for k in range(h):
            res.append(self.NodesAtKdist(root,k))
        return res






    