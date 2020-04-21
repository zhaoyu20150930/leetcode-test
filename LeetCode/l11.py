from typing import List

"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

 



图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

 

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
边界问题，采用双指针，移动边界，获取所有可能情况
x<y 
min(x,y)*t = x*t
移动y t1<t y1<=y min(x,y1)*t1 <= min(x,y)*t y1>y min(x,y1)*t1 = min(x,y)*t = x*t
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        mA = 0
        while i < j:
            mA = max(min(height[i], height[j]) * (j - i), mA)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return mA


if __name__ == '__main__':
    height = [1, 8, 6, 2, 100, 99, 8, 3, 7]
    print(Solution().maxArea(height))
