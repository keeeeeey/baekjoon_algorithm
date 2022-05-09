from itertools import combinations

def solution(needs, r):
    answer = 0
    combs = combinations(range(0, len(needs[0])), r)
    need_cnt_arr = []
    for need in needs:
        need_cnt_arr.append(sum(need));
    for comb in combs:
        temp_ans = 0
        for i in range(len(needs)):
            need_cnt = need_cnt_arr[i]
            temp_cnt = 0
            for idx in comb:
                temp_cnt += needs[i][idx]
            if temp_cnt == need_cnt:
                temp_ans += 1
        answer = max(answer, temp_ans)

    return answer