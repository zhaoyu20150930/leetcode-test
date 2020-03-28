from typing import List

"""
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。

例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。

对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。

那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

 

示例：

输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
 

提示：

1 <= words.length <= 2000
1 <= words[i].length <= 7
每个单词都是小写字母 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minimumLengthEncoding2(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        wd = {}
        for word in words:
            for i in range(len(word) - 1, -1, -1):
                if word[i:] not in wd:
                    wd[word[i:]] = [word]
                else:
                    if len(wd[word[i:]][0]) < len(word):
                        wd[word[i:]].insert(0, word)
                    else:
                        wd[word[i:]].append(word)
        ld = {}
        for word in words:
            mf = wd[word][0]
            if mf in ld:
                ld[mf].append({word: len(mf) - len(word)})
            else:
                ld[mf] = [{word: len(mf) - len(word)}]
        S = ""
        indexes = []
        bl = 0
        for k, v in ld.items():
            S += k + "#"
            for d in v:
                for i in d.values():
                    indexes.append(bl + i)
            bl += len(k) + 1
        print(S,indexes)
        return len(S)


if __name__ == '__main__':
    words = ["time", "me", "bell"]
    print(Solution().minimumLengthEncoding2(words))
