from typing import List

"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]


限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
"""


class Solution:
    def PARENT(self, i):
        return i // 2

    def LEFT(self, i):
        return 2 * i

    def RIGHT(self, i):
        return 2 * i + 1

    def MAX_HEAPIFY(self, A, i, heap_size):
        l = self.LEFT(i)
        r = self.RIGHT(i)
        minimum = i
        if l < heap_size and A[l] > A[i]:
            minimum = l
        if r < heap_size and A[r] > A[minimum]:
            minimum = r
        if minimum != i:
            A[i], A[minimum] = A[minimum], A[i]
            self.MAX_HEAPIFY(A, minimum, heap_size)

    def BUILD_MAX_HEAP(self, A):
        heap_size = len(A)
        for i in range(len(A) // 2, -1, -1):
            self.MAX_HEAPIFY(A, i, heap_size)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        na = arr[0:k]
        self.BUILD_MAX_HEAP(na)
        for k in range(k, len(arr)):
            if na[0] > arr[k]:
                na[0] = arr[k]
                self.MAX_HEAPIFY(na, 0, len(na))
        return na


if __name__ == '__main__':
    arr = [0, 0, 0, 2, 0, 5]
    k = 0
    print(Solution().getLeastNumbers(arr, k))
