def PARENT(i):
    return i // 2


def LEFT(i):
    return 2 * i


def RIGHT(i):
    return 2 * i + 1


def MAX_HEAPIFY(A, i, heap_size):
    l = LEFT(i)
    r = RIGHT(i)
    largest = i
    if l < heap_size and A[l] > A[i]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A, largest, heap_size)


def BUILD_MAX_HEAP(A):
    heap_size = len(A)
    for i in range(len(A) // 2, -1, -1):
        MAX_HEAPIFY(A, i, heap_size)


def HEAP_SORT(A):
    heap_size = len(A)
    BUILD_MAX_HEAP(A)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        MAX_HEAPIFY(A, 0, heap_size)


def MIN_HEAPIFY(self, A, i, heap_size):
    l = self.LEFT(i)
    r = self.RIGHT(i)
    minimum = i
    if l < heap_size and A[l] < A[i]:
        minimum = l
    if r < heap_size and A[r] < A[minimum]:
        minimum = r
    if minimum != i:
        A[i], A[minimum] = A[minimum], A[i]
        self.MIN_HEAPIFY(A, minimum, heap_size)


def BUILD_MIN_HEAP(self, A):
    heap_size = len(A)
    for i in range(len(A) // 2, -1, -1):
        self.MIN_HEAPIFY(A, i, heap_size)


if __name__ == '__main__':
    A = []
    HEAP_SORT(A)
    print(A)
