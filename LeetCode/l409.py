"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""


class Solution:
    def longestPalindrome1(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        lh = 0
        lm = 0
        for k, v in d.items():
            lh += (v // 2) * 2
            d[k] = v % 2
            if d[k] and not lm:
                lm += 1
        return lh + lm

    def longestPalindrome(self, s: str) -> int:
        bs = [0 for _ in range(200)]
        lg = 0
        for i in s:
            if bs[ord(i)] == 0:
                bs[ord(i)] = 1
            else:
                bs[ord(i)] = 0
                lg += 2
        if lg == len(s):
            return lg
        else:
            return lg + 1


if __name__ == '__main__':
    s = "bb"
    print(Solution().longestPalindrome(s))
