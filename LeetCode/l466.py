"""
由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。

如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。

现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。现在考虑字符串 S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。

请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。

 

示例：

输入：
s1 ="acb",n1 = 4
s2 ="ab",n2 = 2

返回：
2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-the-repetitions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        def fm(s1, s2):
            p, q = 0, 0
            for j in range(1, n1 + 1):
                for i in range(0, len(s1)):
                    if s1[i] == s2[p]:
                        p += 1
                    if p == len(s2):
                        q += 1
                        p = 0
                if q > 0:
                    return (j, p, q)
            return (-1, -1, -1)

        def back(s1, s2):
            cc = s1.count(s2)
            for l in range(1, len(s1)):
                if (s1[l:] + s1[0:l]).count(s2) > cc:
                    return True
            return False

        def getM(s3):
            for z in range(0, len(s3)):
                for y in range(0, len(s3), z + 1):
                    if s3[0:z + 1] != s3[y:y + z + 1]:
                        break
                else:
                    return s3[0:z + 1], len(s3) // (z + 1)
            return s3, 1

        s2, n2k = getM(s2)
        n2 = n2k * n2
        s1, n1k = getM(s1)
        n1 = n1k * n1
        j, p, q = fm(s1, s2)  # s1开始匹配，s1结束匹配，s1个数，p结束匹配，q个数
        _, _, vv = fm(s1 * j + s1 * (j - 1), s2)
        if j == - 1:
            return 0
        pn = n1 * q // j
        if back(s1, s2):
            pn = (n1 * q + n1 - 1) // j
        elif vv > q:
            pn = n1 // (j - 1) - 1
        return pn // n2


if __name__ == '__main__':
    s1, n1, s2, n2 = "acb", 1, "acb", 1
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 1)
    s1, n1, s2, n2 = "acb", 12, "cba", 2
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 5)
    s1, n1, s2, n2 = "acb", 10, "acbb", 2
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 2)
    s1, n1, s2, n2 = "acbacb", 4, "ac", 2
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 4)
    s1, n1, s2, n2 = "aaa", 3, "aa", 1
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 4)
    s1, n1, s2, n2 = "baba", 11, "baab", 1
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 7)
    s1, n1, s2, n2 = "bacaba", 3, "abacab", 1
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 2)
    s1, n1, s2, n2 = "nlhqgllunmelayl", 2, "lnl", 1
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 3)
    s1, n1, s2, n2 = "niconiconi", 99981, "nico", 81
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 2468)
    s1, n1, s2, n2 = "phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxf", 100, "xtlsgypsfa", 1
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 49)
    s1, n1, s2, n2 = "phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikef", 1000000, "fmznimkkasvwsrenzkycxfxtlsgypsfad", 333
    print(Solution().getMaxRepetitions(s1, n1, s2, n2), 333)
