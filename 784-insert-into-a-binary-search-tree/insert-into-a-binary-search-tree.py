# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        curr = root
        while True:
            if curr.val < val:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
            else:
                if curr.left is None:
                   curr.left = TreeNode(val)
                   break
                curr = curr.left
        return root
    def preorder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)
                 
    def final(self, root: Optional[TreeNode], val: int) -> List[int]:
        root = self.insertIntoBST(root,val)
        return self.preorder(root)
        