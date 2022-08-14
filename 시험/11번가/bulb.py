def solution(A):
    answer = 0
    l = len(A)
    temp = [0] * (l + 1)
    for i in range(l):
        temp[A[i]] = 1
        flag = True
        for j in range(1, A[i] + 1):
            if temp[j] == 0:
                flag = False
                break

        if flag:
            answer += 1
    return answer

print(solution([2, 1, 3, 5, 4]))
print(solution([2, 3, 4, 1, 5]))
print(solution([1, 3, 4, 2, 5]))