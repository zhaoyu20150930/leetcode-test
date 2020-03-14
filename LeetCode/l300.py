from typing import List

"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sn = sorted(list(set(nums)))
        if not nums:
            return 0
        C = [[0 for _ in range(0, len(sn) + 1)] for _ in range(0, len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for j in range(1, len(sn) + 1):
                if nums[i-1] == sn[j-1]:
                    C[i][j] = C[i - 1][j - 1] + 1
                else:
                    C[i][j] = max(C[i - 1][j], C[i][j - 1])
        print(C)
        return C[-1][-1]


if __name__ == '__main__':
    nums = [3, 2, 1]
    print(Solution().lengthOfLIS(nums))
    nums = [4, 3, 2, 1]
    print(Solution().lengthOfLIS(nums))
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))
    nums = [0]
    print(Solution().lengthOfLIS(nums))
    # nums = []
    # print(Solution().lengthOfLIS(nums))
    nums = [2, 2]
    print(Solution().lengthOfLIS(nums))
    nums = [1, 2]
    print(Solution().lengthOfLIS(nums))
