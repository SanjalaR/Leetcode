# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        self.inorder(root)
        return self.bst(0, len(self.arr)-1)
    def inorder(self, root:TreeNode):
        if not root:
            return
        self.inorder(root.left)
        self.arr.append(root)
        self.inorder(root.right)
    def bst(self, s, e):
        if s>e:
            return None
        m = (s+e)//2
        root = self.arr[m]
        root.left = self.bst(s, m-1)
        root.right = self.bst(m+1, e)
        return root
