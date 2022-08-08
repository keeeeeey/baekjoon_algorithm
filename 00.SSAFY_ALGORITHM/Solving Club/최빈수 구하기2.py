t = int(input())
for tc in range(1, t + 1):
    t_num = int(input())
    scores = list(map(int, input().split()))
    scores_dict = dict()
    for score in scores:
        if score in scores_dict:
            scores_dict[score] += 1
        else:
            scores_dict[score] = 1

    scores_dict_sorted = sorted(scores_dict.items(), key=lambda x: (-x[1], -x[0]))

    print(f"#{tc} {scores_dict_sorted[0][0]}")