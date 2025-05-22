# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None :
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)

    def result(self, root: Optional[TreeNode], val: int) -> List[int]:
        r = self.searchBST(root,val)
        res = self.preorder(r)
        return res