from typing import List

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
二分查找
总是会出现越界问题，在快要下降到边界的时候停止，采用慢速查找
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1s = 0
        n1e = len(nums1)
        n2s = 0
        n2e = len(nums2)
        g = (len(nums1) + len(nums2)) % 2
        m = (len(nums1) + len(nums2)) // 2
        if not g:
            m -= 1
        while n1e > n1s and n2e > n2s and m > 2:
            n1m = n1s + (n1e - n1s) // 2 - 1
            n2m = n2s + (n2e - n2s) // 2 - 1
            if nums1[n1m] < nums2[n2m]:
                m -= n1m - n1s
                n1s = n1m
                n2e = n2m
            else:
                m -= n2m - n2s
                n2s = n2m
                n1e = n1m
        for _ in range(0, m):
            n1 = float('inf')
            n2 = float('inf')
            if n1s < len(nums1):
                n1 = nums1[n1s]
            if n2s < len(nums2):
                n2 = nums2[n2s]
            if n1 > n2:
                n2s += 1
            else:
                n1s += 1
        print(n1s, n2s, m)
        if not g:
            n1 = float('inf')
            n2 = float('inf')
            n3 = float('inf')
            n4 = float('inf')
            if n1s < len(nums1):
                n1 = nums1[n1s]
            if n2s < len(nums2):
                n2 = nums2[n2s]
            if n1s + 1 < len(nums1):
                n3 = nums1[n1s + 1]
            if n2s + 1 < len(nums2):
                n4 = nums2[n2s + 1]
            return float('%.1f' % (min(n1 + n2, n1 + n3, n2 + n4) / 2))
        else:
            n1 = float('inf')
            n2 = float('inf')
            if n1s < len(nums1):
                n1 = nums1[n1s]
            if n2s < len(nums2):
                n2 = nums2[n2s]
            return float('%.1f' % min(n1, n2))


if __name__ == '__main__':
    # 1,2,2,3,3,4,5,8,9,10
    # nums1 = [2, 3, 5, 8, 9, 10]
    # nums2 = [1, 2, 3, 4]
    # print(Solution().findMedianSortedArrays(nums1, nums2))
    # #
    nums1 = [1, 2, 3, 5, 5, 6]
    nums2 = [3, 4, 8, 12, 14]
    # 1,2,3,3,4,5,5,6,8,12,14
    print(Solution().findMedianSortedArrays(nums1, nums2))  # 5
    # nums1 = [1, 3]
    # nums2 = [2]
    # # 1,2,3
    # print(Solution().findMedianSortedArrays(nums1, nums2))
    # nums1 = [1, 2]
    # nums2 = [3, 4]
    # # 1,2,3,4
    # print(Solution().findMedianSortedArrays(nums1, nums2))
    # nums1 = [1]
    # nums2 = [1, 2]
    # # 1,1,2
    # print(Solution().findMedianSortedArrays(nums1, nums2))
    # nums1 = [1, 2, 2]
    # nums2 = [1, 2, 3]
    # # 1,1,2,2,2,3
    # print(Solution().findMedianSortedArrays(nums1, nums2))
    nums1 = [2]
    nums2 = [1, 3, 4]
    # 1,1,2,2,2,3
    print(Solution().findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 2]
    nums2 = [-1, 3]
    print(Solution().findMedianSortedArrays(nums1, nums2))
    # nums1 = [1, 6]
    # nums2 = [2, 3, 4, 5, 7, 8]
    # print(Solution().findMedianSortedArrays(nums1, nums2))
