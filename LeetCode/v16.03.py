from typing import List

"""
给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。

要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。

 

示例 1：

输入：
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
输出： {0.5, 0}
示例 2：

输入：
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
输出： {1, 1}
示例 3：

输入：
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
输出： {}，两条线段没有交点
 

提示：

坐标绝对值不会超过 2^7
输入的坐标均是有效的二维坐标

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        def check(i, j):
            return [i, j] if (start1[0] <= i <= end1[0] or start1[0] >= i >= end1[0]) and (
                    start1[1] <= j <= end1[1] or start1[1] >= j >= end1[1]) and (
                                     start2[0] <= i <= end2[0] or start2[0] >= i >= end2[0]) and (
                                     start2[1] <= j <= end2[1] or start2[1] >= j >= end2[1]) else []

        def findm(start1, end1, start2, end2):
            r = [float('inf'), float('inf')]
            for p in [start1, end1, start2, end2]:
                v = check(p[0], p[1])
                if r[0] > p[0] and v:
                    r = p
                if r[0] == p[0] and r[1] > p[1] and v:
                    r = p
            return r if r[0] != float('inf') else []
        a1 = ((start1[1] - end1[1]) / (start1[0] - end1[0])) if start1[0] != end1[0] else False
        a2 = (start2[1] - end2[1]) / (start2[0] - end2[0]) if start2[0] != end2[0] else False
        b1 = start1[1] - a1 * start1[0]
        b2 = start2[1] - a2 * start2[0]
        if start1[0] == end1[0] and start2[0] != end2[0]:
            b2 = start2[1] - a2 * start2[0]
            i = a2 * start1[0] + b2
            return check(start1[0], i)
        elif start1[0] != end1[0] and start2[0] == end2[0]:
            b1 = start1[1] - a1 * start1[0]
            i = a1 * start2[0] + b1
            return check(start2[0], i)
        elif start1[0] == end1[0] and start2[0] == end2[0]:
            return findm(start1, end1, start2, end2)

        if a1 == a2 and b1 == b2:
            return findm(start1, end1, start2, end2)
        elif a1 == a2:
            return []
        j = (b2 - b1) / (a1 - a2)
        i = a1 * j + b1
        return check(j, i)


if __name__ == '__main__':
    start1, end1, start2, end2 = [0, 0], [1, 1], [2, 2], [3, 3]
    print(Solution().intersection(start1, end1, start2, end2))
