"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        A = [[0 for _ in range(0, len(word2) + 1)] for _ in range(0, len(word1) + 1)]
        for i in range(0, len(word2) + 1):
            A[0][i] = i
        for j in range(0, len(word1) + 1):
            A[j][0] = j
        for i in range(0, len(word1)):
            for j in range(0, len(word2)):
                if word1[i] == word2[j]:
                    A[i + 1][j + 1] = A[i][j]
                else:
                    A[i + 1][j + 1] = min(A[i][j + 1], A[i + 1][j], A[i][j]) + 1
        return A[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))
    word1 = "intention"
    word2 = "execution"
    print(Solution().minDistance(word1, word2))
    word1 = "ohrbs"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))
