def COMPUTE_TRANSITION_FUNCTION(P, E):
    """
    转移函数
    :param P: 匹配模式
    :param E: 输入字母表
    :return:
    """
    o = {}
    m = len(P)
    q = 0
    while q < m:

        for a in E:
            k = min(m + 1, q + 2)
            while k > 0:
                k -= 1
                if P[0:k] == P[q - k + 1:q] + a:
                    break
            o["{}-{}".format(q, a)] = k
        q += 1

    def O(q, a):
        return o["{}-{}".format(q, a)]

    return O, m


def FINITE_AUTOMATION_MATCHER(T, O, m):
    """
    文本匹配状态机
    :param T: 文本
    :param o: 状态转移函数
    :param m: 唯一接收状态
    :return:
    """
    global j
    n = len(T)
    q = 0
    for i in range(0, n):
        q = O(q, T[i])
        if q == 0:
            j = i + 1
        if q == m:
            print(j, i, T[j:i + 1])


if __name__ == '__main__':
    T = "kdkdslzhaoyu"
    P = 'zhaoyu'
    O, m = COMPUTE_TRANSITION_FUNCTION(P, set(T))
    FINITE_AUTOMATION_MATCHER(T, O, m)
