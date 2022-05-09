def solution(scores):
    answer = 0
    N = len(scores[0])
    dic = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
    for score in scores:
        F_cnt = 0
        A_cnt = 0
        minV = 6
        maxV = 0
        total = 0
        for s in score:
            total += dic[s]
            if dic[s] < minV:
                minV = dic[s]
            if dic[s] > maxV:
                maxV = dic[s]
            if s == "F":
                F_cnt += 1
            elif s == "A":
                A_cnt += 1

        if F_cnt >= 2:
            continue
        if A_cnt >= 2:
            answer += 1
            continue
        total -= minV
        total -= maxV
        avg = total / (N - 2)
        if avg >= 3:
            answer += 1

    return answer