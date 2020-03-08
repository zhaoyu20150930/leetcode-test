from typing import List

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
 
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def inBlackPoint(self, row: int, line: int, black_point: List[List[int]]) -> bool:
        for bp in black_point:
            if bp[1] == line:
                return True
            if abs(bp[1] - line) == abs(bp[0] - row):
                return True
        return False

    def nQ(self, N: List[List[int]], n: int, row: int, rel: List[List[str]], black_point: List[List[int]]):
        if row == n:
            N_copy = ["".join(["Q" if N[p][q] else "." for q in range(n)]) for p in range(n)]
            rel.append(N_copy)
            return
        for l in range(0, n):
            if not self.inBlackPoint(row, l, black_point):
                N_copy = [[N[p][q] for q in range(n)] for p in range(n)]
                N_copy[row][l] = 1
                black_point_copy = [[bp[0], bp[1]] for bp in black_point]
                black_point_copy.append([row, l])
                self.nQ(N_copy, n, row + 1, rel, black_point_copy)

    def solveNQueens(self, n: int) -> List[List[str]]:
        rel = []
        self.nQ([[0 for _ in range(n)] for _ in range(n)], n, 0, rel, [])
        return rel


if __name__ == '__main__':
    print(Solution().solveNQueens(5))
