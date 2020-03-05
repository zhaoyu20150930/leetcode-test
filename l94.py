# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def visit(self, node: TreeNode, l: List[int]):
        if node and node.left:
            self.visit(node.left, l)
        if node:
            l.append(node.val)
        if node and node.right:
            self.visit(node.right, l)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        self.visit(root, l)
        return l
