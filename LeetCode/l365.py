"""
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False
"""


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        seen = set()
        while stack:
            rx, ry = stack.pop()
            if rx + ry == z or rx == z or ry == z:
                return True
            if (rx, ry) in seen:
                continue
            seen.add((rx, ry))
            stack.append((x, ry))
            stack.append((rx, y))
            stack.append((rx, 0))
            stack.append((0, ry))
            stack.append((rx - min(rx, y - ry), ry + min(rx, y - ry)))
            stack.append((rx + min(ry, x - rx), ry - min(ry, x - rx)))
        return False


if __name__ == '__main__':
    # x = 3
    # y = 5
    # z = 4
    # print(Solution().canMeasureWater(x, y, z))  # True
    #
    # x = 2
    # y = 6
    # z = 5
    # print(Solution().canMeasureWater(x, y, z))  # False
    #
    # x = 0
    # y = 0
    # z = 0
    # print(Solution().canMeasureWater(x, y, z))  # False
    #
    # x = 1
    # y = 2
    # z = 3
    # print(Solution().canMeasureWater(x, y, z))  # False
    #
    # x = 0
    # y = 0
    # z = 1
    # print(Solution().canMeasureWater(x, y, z))  # False

    x = 34
    y = 5
    z = 6
    print(Solution().canMeasureWater(x, y, z))  # False
