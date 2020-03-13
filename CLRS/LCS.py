from typing import List


def LCS(X: str, Y: str):
    C = [[0 for _ in range(0, len(Y))] for _ in range(0, len(X))]
    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if X[i] == Y[j]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i - 1][j], C[i][j - 1])
    beauty_print(C)
    PRINT_LCS(C, X, Y)


def LCS_BACK(X: str, Y: str, i: int, j: int, C: List[List[int]]):
    if i <= 0 or j <= 0:
        return
    if C[i - 1][j - 1] == 0:
        LCS_BACK(X, Y, i - 1, j - 1, C)
    if C[i][j - 1] == 0:
        LCS_BACK(X, Y, i, j - 1, C)
    if C[i - 1][j] == 0:
        LCS_BACK(X, Y, i - 1, j, C)
    if X[i] == Y[j]:
        C[i][j] = C[i - 1][j - 1] + 1
    else:
        C[i][j] = max(C[i - 1][j], C[i][j - 1])


def PRINT_LCS(C, X, Y):
    i = len(X) - 1
    j = len(Y) - 1

    while i > 0 and j > 0:
        if C[i - 1][j] >= C[i][j - 1] and C[i - 1][j] > C[i - 1][j - 1]:
            i -= 1
        elif C[i - 1][j - 1] >= C[i - 1][j] and C[i - 1][j - 1] >= C[i][j - 1]:
            print(X[i])
            i -= 1
            j -= 1
        elif C[i][j - 1] > C[i - 1][j] and C[i][j - 1] > C[i - 1][j - 1]:
            j -= 1


def beauty_print(C):
    print("[")
    for l in C:
        print(l)
    print("]")


if __name__ == '__main__':
    X = "ABCBDABDDDDDDD"
    Y = "BDCABADDFDD"
    LCS(X, Y)
    C = [[0 for _ in range(0, len(Y))] for _ in range(0, len(X))]
    i, j = len(X) - 1, len(Y) - 1
    LCS_BACK(X, Y, i, j, C)
    beauty_print(C)
    PRINT_LCS(C, X, Y)
