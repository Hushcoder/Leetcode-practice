# from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        poss_paths = []
        def dfs(root, current_path):
            if root is None:
               return 

            current_path.append(str(root.val))
    
            if not root.left and not root.right:
               poss_paths.append(''.join(map(str, current_path)))
        
            dfs(root.left, current_path)
            dfs(root.right, current_path)

            current_path.pop()

            return poss_paths

        tTostr = dfs(root, []) # ['001', '101' ....]
        # traversal in str
        return sum(int(path, 2) for path in poss_paths)
 
        
        # self._node_ls = []
        # self._node_dq = deque([root]) 

        # while self._node_dq:
        #     self._current_node = self._node_dq.popleft()
        #     self._node_ls.append(self._current_node.val)

        #     if self._current_node.left:
        #         self._node_dq.append(self._current_node.left)
        #     if self._current_node.right:
        #         self._node_dq.append(self._current_node.right)

        # return ''.join(map(str, self._node_ls))


        

        
            
