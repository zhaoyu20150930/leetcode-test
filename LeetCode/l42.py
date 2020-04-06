from typing import List

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]
        for i in range(0, len(height)):
            leftMax.append(max(leftMax[- 1], height[i]))

        rightMax = [0]
        for j in range(len(height) - 1, -1, -1):
            rightMax.append(max(rightMax[-1], height[j]))
        r = 0
        for k in range(0, len(height)):
            r += min(leftMax[k+1],rightMax[len(rightMax)-k-1]) - height[k]
        return r

    def trap2(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        hi = []
        for i in range(0, len(height)):
            hi.append((height[i], i))
        hi.sort(key=lambda x: x[0], reverse=True)
        x, y = hi[0]
        z, k = 0, 0
        for i in range(1, len(hi)):
            if y > hi[i][1] and not z:
                z = i
            if y < hi[i][1] and not k:
                k = i
            if z and k:
                break
        b = min(hi[z][0], x)
        c = min(hi[k][0], x)
        q = 0
        for i in range(hi[z][1] + 1, y):
            if b > height[i]:
                q += b - height[i]
        for i in range(y, hi[k][1]):
            if c > height[i]:
                q += c - height[i]
        return q + self.trap2(height[0:hi[z][1] + 1]) + self.trap2(height[hi[k][1]:len(height)])


if __name__ == '__main__':
    height = [11, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 10]
    print(Solution().trap(height))
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))
