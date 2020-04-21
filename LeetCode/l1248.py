from typing import List

"""
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def isOdd(n):
            return n % 2 == 1

        nl = len(nums)
        odps = [i for i in range(0, nl) if isOdd(nums[i])]
        c, ol = 0, len(odps)
        for i in range(k - 1, ol):
            r, t = i - k + 1, i
            p, q = odps[r], odps[t]
            if r - 1 >= 0:
                n = p - odps[r - 1]
            else:
                n = p + 1
            if t + 1 < ol:
                z = odps[t + 1] - q
            else:
                z = nl - q
            c += n * z
        return c


if __name__ == '__main__':
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(Solution().numberOfSubarrays(nums, k))
    nums = [2, 4, 6]
    k = 1
    print(Solution().numberOfSubarrays(nums, k))
    nums = [2, 2, 2, 1, 2, 2, 1, 2, 1, 2]
    k = 2
    print(Solution().numberOfSubarrays(nums, k))
