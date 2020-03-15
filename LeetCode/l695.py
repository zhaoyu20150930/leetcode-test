from typing import List

"""
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-area-of-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        d = [[] for _ in range(0, len(grid) * len(grid[0]) + 1)]
        k = 1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    dl, dt = 0, 0
                    if i > 0:
                        dl = grid[i - 1][j]
                    if j > 0:
                        dt = grid[i][j - 1]
                    if dl > 0 or dt > 0:
                        if dl == dt:
                            grid[i][j] = dl
                            d[dt].append((i, j))
                        else:
                            if dl > 0:
                                for di in d[dt]:
                                    grid[di[0]][di[1]] = dl
                                    d[dl].append(di)
                                grid[i][j] = dl
                                d[dl].append((i, j))
                                d[dt].clear()
                            else:
                                for di in d[dl]:
                                    grid[di[0]][di[1]] = dt
                                    d[dt].append(di)
                                grid[i][j] = dt
                                d[dt].append((i, j))
                                d[dl].clear()
                    else:
                        d[k].append((i, j))
                        grid[i][j] = k
                        k += 1
        maxdi = 0
        for di in d:
            if len(di) > maxdi:
                maxdi = len(di)
        return maxdi


if __name__ == '__main__':
    grid = [[1]]

    print(Solution().maxAreaOfIsland(grid))
