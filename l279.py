"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
    T(n) = min(T(n-i*i)) + 1 1<i<n**0.5
"""


class Solution:
    def numSquares(self, n: int) -> int:
        seq = [0, ] * (n + 1)
        sq = 1
        for i in range(1, n + 1):
            if i == sq * sq:
                seq[i] = 1
                sq += 1
            else:
                for j in range(1, int(i * 0.5) + 1):
                    x, y = j, i - j
                    seq_v = seq[x] + seq[y]
                    if seq_v < seq[i] or seq[i] == 0:
                        seq[i] = seq_v
        return seq[-1]

    def numSquares2(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, int(i ** (0.5)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numSquares2(7168))
