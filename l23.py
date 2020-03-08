from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def parent(self, i: int) -> int:
        return i // 2

    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def min_heapify(self, a: List[ListNode], i: int):
        l = self.left(i)
        r = self.right(i)
        if l < len(a) and a[l].val < a[i].val:
            minmum = l
        else:
            minmum = i
        if r < len(a) and a[minmum].val > a[r].val:
            minmum = r
        if minmum != i:
            a[minmum], a[i] = a[i], a[minmum]
            self.min_heapify(a, minmum)

    def min(self, a: List[ListNode]) -> ListNode:
        return a[0]

    def build_heap(self, a: List[ListNode]):
        for i in range(len(a) // 2, -1, -1):
            self.min_heapify(a, i)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        lists = [ln for ln in lists if ln]
        if not lists:
            return head.next
        a = [ln for ln in lists]
        self.build_heap(a)

        pre = head
        while True:
            m = self.min(a)
            if isinstance(m.val, float):
                return head.next
            if m.next:
                a[0] = m.next
                self.min_heapify(a, 0)
            else:
                a[0] = ListNode(float('inf'))
                self.min_heapify(a, 0)
            pre.next = m
            pre = m


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)

    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)

    c = ListNode(2)
    c.next = ListNode(6)
    lists = [[]]
    print(Solution().mergeKLists(lists))
