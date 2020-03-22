from typing import List
from LeetCode.l954r import AL

"""
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。

返回使 A 中的每个值都是唯一的最少操作次数。

示例 1:

输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
示例 2:

输入：[3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
提示：

0 <= A.length <= 40000
0 <= A[i] < 40000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def ac(self, A, O, b):
        for a in A:
            p = a // 32
            i = a % 32
            if (1 << i & b[p]) != 0:
                O.append(a)
            else:
                b[p] |= 1 << i


    def minIncrementForUnique(self, A: List[int]) -> int:
        b = [0 for _ in range(2500)]
        O = []
        self.ac(A, O, b)
        O.sort()
        n = 0
        c = 0
        q = 0
        while q < 80000:
            if n == len(O):
                break
            p = q // 32
            if q % 32 == 0 and b[p] == b'11111111111111111111111111111111':
                q += 32
            i = q % 32
            if (1 << i & b[p]) == 0:
                if q > O[n]:
                    c += q - O[n]
                    n += 1
            q += 1
        return c


if __name__ == '__main__':
    # A = [2, 2, 2]
    # assert Solution().minIncrementForUnique(A) == 0
    # A = [3, 2, 1, 2, 1, 7]
    # assert Solution().minIncrementForUnique(A) == 6

    print(Solution().minIncrementForUnique(AL) == 3905021)
