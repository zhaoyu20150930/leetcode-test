"""
设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

示例：

LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class LFUCache:
    class Node:
        def __init__(self, key, val, next, pre, freq):
            self.key = key
            self.val = val
            self.next = next
            self.pre = pre
            self.freq = freq

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.size = 0
        self.f = {}
        self.minN = None

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            n.pre.next = n.next
            n.next.pre = n.pre
            on = self.f[n.freq + 1]
            n.next = on
            on.pre = n
            n.pre = None
            self.f[n.freq + 1] = n
            
        else:
            return -1

    def addN(self, nn):
        if 1 in self.f:
            on = self.f[1]
            nn.next = on
            on.pre = nn
            self.f[1] = nn
        else:
            self.f[1] = nn
            self.minN = nn

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            nn = LFUCache.Node(key, value, None, None, 1)
            if self.size < self.capacity:
                self.addN(nn)
                self.size += 1
            else:
                self.addN(nn)


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # 返回1
    cache.put(3, 3)  # 去除key 2
    cache.get(2)  # 返回 - 1(未找到key 2)
    cache.get(3)  # 返回 3
    cache.put(4, 4)  # 去除 key 1
    cache.get(1)  # 返回 - 1(未找到 key 1)
    cache.get(3)  # 返回3
    cache.get(4)  # 返回4
