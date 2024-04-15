# Given the root of a binary tree, return all root-to-leaf paths in any order.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, res, path):
            if root==None:
                return
            res += str(root.val)
            if(root.left==None and root.right==None):
                path.append(res)
            else:
                dfs(root.left, res+'->', path)
                dfs(root.right, res+'->', path)
                
        path = []
        dfs(root, '', path)
        return path
