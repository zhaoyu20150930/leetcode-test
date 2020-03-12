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

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        a = []
        l = []
        if not root:
            return a
        l.append(root)
        s = set()
        while l:
            n = l.pop()
            if n not in s:
                if n.right:
                    l.append(n.right)
                l.append(n)
                if n.left:
                    l.append(n.left)
            else:
                a.append(n.val)

            s.add(n)
        return a

    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        pass

if __name__ == '__main__':
    r = TreeNode(1)
    r.right = TreeNode(2)
    r.right.left = TreeNode(3)
    Solution().inorderTraversal3(r)
