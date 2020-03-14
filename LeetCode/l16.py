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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
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

    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        exi = [-1, -1, -1]
        f = target * -1
        g = 0
        for j in range(0, 3):
            n = True
            for i in range(0, len(nums)):
                if i in exi:
                    continue
                if abs(nums[i] + f) < abs(g) or n:
                    n = False
                    g = nums[i] + f
                    exi[j] = i
            f = g
        print(exi)
        return f + target


if __name__ == '__main__':
    nums = [13, 34, 8, 91, 0, -47, 52, 23, 76, 14, 0, -9, 22, 49, -1, 68, 49, -83, -34, 5, 38, 3, 47, -2, -73, -29, 19,
            -4, -3, -16, 89, 52, 18, 27, 40, 88, -84, -68, 84, 53, 52, 28, -86, -80, 18, -93, 11, 77, 11, -83, 69, -29,
            -26, -83, 32, 65, -49, -88, -24, -56, 95, -82, -25, -69, -27, 20, -87, -49, 78, 89, 100, 26, 45, -15, 47,
            77, 86, 46, 82, -80, -31, 72, -82, -63, -50, 35, -36, -30, -40, 82, 83, -61, -49, -11, 88, 73, -23, 2, 63,
            29, -82, 95, -91, 31, -35, -84, 37, -86, -17, -84, -54, -89, 32, 13, -21, 73, -73, 53, -57, -60, 62, -43,
            54, 52, 91, -7, 23, -53, 53, -82, -75, 43, 21, 76, 45, -2, -46, -39, -39, -3, 24, 6, -73, 34, 58, -67, 35,
            45, -72, -67, -57, -22, -81, 68, -84, -15, 14, -87, 14, -45, -68, 4, -88, -25, -36, -74, -27, 27, -23, 26,
            -99, -47, 97, 32, 53, 82, -89, 91, -1, -67, -74, -97, -36, 7, -51, -100, -74, 28, -12, -46, -37, 87, 80,
            -33, -58, 51, 5]
    nums = [0, 2, 1, -3]
    target = 1
    import time

    start = time.time()
    print(Solution().threeSumClosest1(nums, target))
    print(time.time() - start)
