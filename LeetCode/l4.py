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


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1s = 0
        n1e = len(nums1) - 1
        n2s = 0
        n2e = len(nums2) - 1
        gcd = (len(nums2) + len(nums1)) % 2
        if not gcd:
            m = (len(nums1) + len(nums2)) // 2 - 1
        else:
            m = (len(nums1) + len(nums2)) // 2
        while m > 0 and nums1[n1s:n1e + 1] and nums2[n2s:n2e + 1]:
            n1m = n1s + (n1e - n1s) // 2
            n2m = n2s + (n2e - n2s) // 2
            if nums1[n1m] < nums2[n2m]:
                m -= n1m - n1s
                if n1s != n1m:
                    n1s = n1m
                else:
                    n1s += n1m + 1
                    m -= 1
                n2e = n2m
            else:
                m -= n2m - n2s
                if n2s != n2m:
                    n2s = n2m
                else:
                    n2s += n2m + 1
                    m -= 1
                n1e = n1m
            print(nums1[n1s:n1e + 1], nums2[n2s:n2e + 1], m)
        print(n1s, n1e, n2s, n2e)
        if m == 0:
            if gcd == 0:
                m1 = float("inf")
                if n1s + 1 < len(nums1):
                    m1 = (nums1[n1s] + nums1[n1s + 1]) / 2
                m2 = float("inf")
                if n2s + 1 < len(nums2):
                    m2 = (nums2[n2s] + nums2[n2s + 1]) / 2
                m3 = float("inf")
                if n2s < len(nums2) and n1s < len(nums1):
                    m3 = (nums1[n1s] + nums2[n2s]) / 2
                return float('%.1f' % min(m1, m2, m3))
            else:
                m1 = float("inf")
                if n1s < len(nums1):
                    m1 = nums1[n1s]
                m2 = float("inf")
                if n2s < len(nums2):
                    m2 = nums2[n2s]
                return float('%.1f' % min(m1, m2))
        else:
            if not nums1[n1s:n1e + 1]:
                if gcd == 0:
                    return float('%.1f' % ((nums2[n2s + m] + nums2[n2s + m + 1]) / 2))
                else:
                    return float('%.1f' % nums2[n2s + m])
            elif not nums2[n2s:n2e + 1]:
                if gcd == 0:
                    return float('%.1f' % ((nums1[n1s + m] + nums1[n1s + m + 1]) / 2))
                else:
                    return float('%.1f' % nums1[n1s + m])


if __name__ == '__main__':
    # 1,2,2,3,3,4,5,8,9,10
    nums1 = [2, 3, 5, 8, 9, 10]
    nums2 = [1, 2, 3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
    # #
    # nums1 = [1, 2, 3, 5, 5, 6]
    # nums2 = [3, 4, 8, 12, 14]
    # # 1,2,3,3,4,5,5,6,8,12,14
    # print(Solution().findMedianSortedArrays(nums1, nums2))
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
    # nums1 = [2]
    # nums2 = [1, 3, 4]
    # # 1,1,2,2,2,3
    # print(Solution().findMedianSortedArrays(nums1, nums2))
