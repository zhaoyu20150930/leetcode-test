"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree_minimum(self, node: TreeNode) -> TreeNode:
        n = node
        while n.left:
            n = n.left
        return n

    def node_parent(self, parent: TreeNode, node: TreeNode) -> TreeNode:
        if parent:
            if parent.left and parent.left.val == node.val:
                return parent
            if parent.right and parent.right.val == node.val:
                return parent
        if parent:
            node_left = self.node_parent(parent.left, node)
            node_right = self.node_parent(parent.right, node)
            if node_left:
                return node_left
            if node_right:
                return node_right

    def tree_successor(self, x: TreeNode, r: TreeNode) -> TreeNode:
        if x.right:
            return self.tree_minimum(x.right)
        y = self.node_parent(r, x)
        while y and x == y.right:
            x = y
            y = self.node_parent(r, x)
        return y

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        n = self.tree_minimum(root)
        if not n:
            return
        break_node1, break_node2 = None, None
        while n:
            node_successor = self.tree_successor(n, root)
            if node_successor:
                if n.val > node_successor.val and not break_node1:
                    break_node1 = n
                    break_node2 = node_successor
                elif n.val > node_successor.val:
                    break_node2 = node_successor
            n = node_successor
        break_node2.val, break_node1.val = break_node1.val, break_node2.val


if __name__ == '__main__':
    r = TreeNode(3)
    r.left = TreeNode(1)
    r.right = TreeNode(4)
    r.right.left = TreeNode(2)
    Solution().recoverTree(r)
    print(r)
