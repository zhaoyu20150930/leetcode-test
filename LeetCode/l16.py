from typing import List

"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        m = abs(nums[0] + nums[1] + nums[2] - target)
        m1, m2, m3 = nums[0], nums[1], nums[2]
        s = set()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) in s:
                    continue
                s.add(nums[i] + nums[j])
                for k in range(j + 1, len(nums)):
                    if m > abs(nums[i] + nums[j] + nums[k] - target):
                        m1, m2, m3 = nums[i], nums[j], nums[k]
                        m = abs(nums[i] + nums[j] + nums[k] - target)
                        if m == 0:
                            break
        return m1 + m2 + m3

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        mm = 100000
        for j in range(0, len(nums) - 1):
            i, k = j + 1, len(nums) - 1
            d = nums[i] + nums[j] + nums[k] - target
            while True:
                ds = 1 if d < 0 else -1
                nj = nk = ni = nums[i] + nums[j] + nums[k] - target
                mj = mk = mi = False
                if 0 <= i + ds < j:
                    ni = nums[i + ds] + nums[j] + nums[k] - target
                    mi = True
                if i < j + ds < k:
                    nj = nums[i] + nums[j + ds] + nums[k] - target
                    mj = True
                if j < k + ds < len(nums):
                    nk = nums[i] + nums[j] + nums[k + ds] - target
                    mk = True
                if abs(nk) <= abs(ni) and abs(nk) <= abs(nj) and mk:
                    k += ds
                elif abs(nj) <= abs(ni) and abs(nj) <= abs(nk) and mj:
                    j += ds
                elif abs(ni) <= abs(nj) and abs(ni) <= abs(nk) and mi:
                    i += ds
                if abs(d) <= abs(nums[i] + nums[j] + nums[k] - target):
                    break
                d = nums[i] + nums[j] + nums[k] - target
                if abs(d) < abs(mm):
                    mm = d
        return mm


if __name__ == '__main__':
    nums = [-4, -1, 1, 2]
    target = 1
    print(Solution().threeSumClosest(nums, target))  # 2
    # nums = [1, 1, -1, -1, 3]
    # target = 1
    # print(Solution().threeSumClosest(nums, target))  # 1
    # nums = [-1, 0, 1, 2, -1, -4]
    # target = 0
    # print(Solution().threeSumClosest(nums, target))  # 0
