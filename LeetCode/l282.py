from typing import List

"""
给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例 1:

输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"] 
示例 2:

输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
示例 3:

输入: num = "105", target = 5
输出: ["1*0+5","10-5"]
示例 4:

输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]
示例 5:

输入: num = "3456237490", target = 9191
输出: []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/expression-add-operators
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def cal(self, num: str, target: int, start: int, seq: List[int], seqm: str, l: List[str]):
        if len(num) == start:
            c = 0
            for s in seq:
                c += s
            if c == target:
                l.append(seqm)
            return
        if len(seq) > 0:
            for j in range(start, len(num)):
                addSeq = [s for s in seq]
                addSeq.append(int(num[start:j + 1]))
                self.cal(num, target, j + 1, addSeq, seqm + "+" + num[start:j + 1], l)

                subSeq = [s for s in seq]
                subSeq.append(int(num[start:j + 1]) * -1)
                self.cal(num, target, j + 1, subSeq, seqm + "-" + num[start:j + 1], l)

                mulSeq = [s for s in seq]
                v = mulSeq.pop()
                mulSeq.append(int(num[start:j + 1]) * v)
                self.cal(num, target, j + 1, mulSeq, seqm + "*" + num[start:j + 1], l)
                if num[start] == '0':
                    break

        else:
            for j in range(start, len(num)):
                nseq = [s for s in seq]
                nseq.append(int(num[start:j + 1]))
                self.cal(num, target, j + 1, nseq, seqm + num[start:j + 1], l)
                if num[start] == '0':
                    break

    def addOperators(self, num: str, target: int) -> List[str]:
        l = []
        self.cal(num, target, 0, [], "", l)
        return l

    def addOperatorsg(self, num: 'str', target: 'int') -> 'List[str]':

        N = len(num)
        answers = []

        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            if index == N:

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand * 10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:
                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            string.append('+');
            string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();
            string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:
                # SUBTRACTION
                string.append('-');
                string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();
                string.pop()

                # MULTIPLICATION
                string.append('*');
                string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0,
                        value - prev_operand + (current_operand * prev_operand), string)
                string.pop();
                string.pop()

        recurse(0, 0, 0, 0, [])
        return answers


if __name__ == '__main__':
    # assert Solution().addOperators("2147483648", -2147483648) == ["1*0+5", "10-5"]
    # assert Solution().addOperators("000", 0) == ["0*0*0","0*0+0","0*0-0","0+0*0","0+0+0","0+0-0","0-0*0","0-0+0","0-0-0"]
    # assert Solution().addOperators("105", 5) == ["1*0+5", "10-5"]
    # assert Solution().addOperators("123", 6) == ["1+2+3", "1*2*3"]
    # assert Solution().addOperators("232", 8) == ["2*3+2", "2+3*2"]
    # assert Solution().addOperators("00", 0) == ["0+0", "0-0", "0*0"]
    import time

    start = time.time()
    assert Solution().addOperators("3456237490", 9191) == []
    print(time.time() - start)
