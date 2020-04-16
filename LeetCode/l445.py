"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lp1, lp2 = [], []
        hl1, hl2 = l1, l2
        while hl1 or hl2:
            if hl1:
                lp1.append(hl1)
                hl1 = hl1.next
            if hl2:
                lp2.append(hl2)
                hl2 = hl2.next
        j = 0
        h = None
        while lp2 or lp1 or j>0:
            a = lp2.pop().val if lp2 else 0
            b = lp1.pop().val if lp1 else 0
            c = a + b + j
            j = 1 if c > 9 else 0
            n = ListNode(c % 10)
            n.next = h
            h = n
        return h


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    ls = Solution().addTwoNumbers(None, None)
    while ls:
        print(ls.val)
        ls = ls.next
