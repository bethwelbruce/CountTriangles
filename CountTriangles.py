def solution(A):
    A.sort()
    count = 0
    for p in range(len(A)-2):
        r = p+2
        for q in range(p+1, len(A)-1):
            while r < len(A) and A[p] + A[q] > A[r]:
                r += 1
            count += r - q - 1
    return count