def QUICK_SORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)
        QUICK_SORT(A, p, q - 1)
        QUICK_SORT(A, q + 1, r)


def PARTITION(A, p, r):
    i = p - 1
    x = A[r]
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == '__main__':
    A = list(range(10000))
    QUICK_SORT(A, 0, len(A) - 1)
    print(A)
