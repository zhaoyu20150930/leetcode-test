from typing import List

"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0], reverse=True)
        s = []
        while intervals:
            if s:
                i, j = s.pop()
                p, q = intervals.pop()
                if j >= p:
                    s.append((min(i, p), max(j, q)))
                else:
                    s.append((i, j))
                    s.append((p, q))
            else:
                s.append(intervals.pop())
        return s


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [6, 7], [8, 10], [15, 18], [18, 20]]
    print(Solution().merge(intervals))
    intervals = [[1, 4], [4, 5]]
    print(Solution().merge(intervals))
    intervals = [[1, 4], [2, 3]]
    print(Solution().merge(intervals))
    intervals = [[1, 4], [0, 3]]
    print(Solution().merge(intervals))
    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    print(Solution().merge(intervals))
