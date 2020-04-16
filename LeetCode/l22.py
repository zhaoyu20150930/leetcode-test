from typing import List

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def f(self, nl, nf, a, A):
        if nl == 0 and nf == 0:
            A.append(a)
            return
        if nl == nf:
            self.f(nl - 1, nf, a + '(', A)
        else:
            if nl > 0:
                self.f(nl - 1, nf, a + '(', A)
            if nf > 0:
                self.f(nl, nf - 1, a + ')', A)

    def generateParenthesis(self, n: int) -> List[str]:
        A = []
        a = ''
        self.f(n, n, a, A)
        return A


if __name__ == '__main__':
    n = 4
    ls = Solution().generateParenthesis(n)
    for l in ls:
        print(l)
