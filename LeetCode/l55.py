from typing import List

"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        最大覆盖范围
        :param nums:
        :return:
        """
        if not nums:
            return False
        mf = 0
        L = len(nums)
        for i in range(0, L):
            if mf < i:
                return False
            mf = max(mf, nums[i] + i)
        return True

    def canJump1(self, nums: List[int]) -> bool:
        """
        DFS,BFS
        :param nums:
        :return:
        """
        A = [0] if nums else []
        E = set()
        while A:
            nA = []
            for j in A:
                if j == len(nums) - 1:
                    return True
                r = nums[j]
                for i in range(j + 1, min(j + nums[j] + 1, len(nums))):
                    if i not in E:
                        nA.append(i)
                        E.add(i)
                    r -= 1
                    if r <= nums[i]:
                        break
            A = nA
        return False


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().canJump(nums))
    nums = [3, 4, 1, 0, 4]
    print(Solution().canJump(nums))
    nums = [2, 1, 0, 1]
    print(Solution().canJump(nums))
    nums = [i for i in range(25000, 0, -1)]
    nums.append(1)
    nums.append(0)
    nums.append(1)
    print(Solution().canJump(nums))
