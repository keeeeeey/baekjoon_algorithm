def solution(p):
    answer = [0] * len(p)
    for i in range(len(p)):
        min_idx = i

        if p[i] != i + 1:
            answer[i] += 1

        for j in range(i + 1, len(p)):
            if p[min_idx] > p[j]:
                min_idx = j

        if p[min_idx] != min_idx + 1:
            answer[min_idx] += 1
        p[i], p[min_idx] = p[min_idx], p[i]
    return answer

print(solution([2, 5, 3, 1, 4]))