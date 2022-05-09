def solution(A, B):
    # write your code in Python 3.6
    base = str(A)
    M = len(base)
    s = str(B)
    N = len(s)
    for i in range(N - M + 1):
        for j in range(M):
            if base[j] != s[i + j]:
                break
        else:
            return i
    return -1

def solution(A):
    # write your code in Python 3.6
    ans_cnt = 0
    maxV = 0
    for i in range(len(A)):
        maxV = max(maxV, A[i])
        if maxV == i + 1:
            ans_cnt += 1
    return ans_cnt