from typing import List

"""
给定一个整数数组 nums，将该数组升序排列。

 

示例 1：

输入：[5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：[5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= A.length <= 10000
-50000 <= A[i] <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def middle3(self, p, r, nums):
        m = p + (r - p) // 2
        if nums[m] > nums[p] and nums[m] > nums[r - 1]:
            return m
        if nums[p] > nums[m] and nums[p] > nums[r - 1]:
            return p
        return r - 1

    def partion(self, p, r, nums):
        m = self.middle3(p, r, nums)
        nums[m], nums[r - 1] = nums[r - 1], nums[m]
        x = nums[r - 1]
        i = p - 1
        for j in range(p, r):
            if x > nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r - 1] = nums[r - 1], nums[i + 1]
        return i + 1

    def sortArray(self, nums: List[int]) -> List[int]:
        pks = [(0, len(nums))]
        while pks:
            p, r = pks.pop()
            if p < r:
                q = self.partion(p, r, nums)
                pks.append((p, q))
                pks.append((q + 1, r))
        return nums


if __name__ == '__main__':
    nums = [5, 1, 1, 2, 0, 0]
    print(Solution().sortArray(nums))
    nums = [5, 2, 3, 1]
    print(Solution().sortArray(nums))
    nums = list(range(10000, 0, -1))
    print(nums)
    print(Solution().sortArray(nums))
