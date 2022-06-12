def solution(data):
    answer = []
    scores = []
    best_list = []
    worst_list = []
    for i in range(7):
        weather_score = 0

        if data[i][0] == 1 or data[i][0] == 2:
            weather_score = 20
        elif data[i][0] == 3:
            weather_score = 17
        elif data[i][0] == 4:
            worst_list.append(i)
            weather_score = 10

        if data[i][1] == 1:
            worst_list.append(i)
            weather_score = 5
        elif data[i][1] == 2:
            weather_score = 14
        scores.append(weather_score)

        if 0 >= data[i][2] or 30 <= data[i][2]:
            worst_list.append(i)
        temper_score = 20 - abs(22 - data[i][2])
        scores[i] += temper_score

    answer = select_best_day(scores, best_list, answer)
    answer = select_worst_day(scores, worst_list, answer)

    return answer

def select_best_day(scores, best_list, answer):
    max_score = max(scores)

    for i in range(7):
        if scores[i] == max_score:
            best_list.append(i)

    priority = [5, 4, 6, 2, 3, 1, 0]

    if len(best_list) == 1:
        answer.append(best_list[0])
    else:
        for i in range(7):
            for best in best_list:
                if best == priority[i]:
                    answer.append(best)
                    break
            if len(answer) == 1:
                break

    return answer

def select_worst_day(scores, worst_list, answer):
    min_score = int(1e9)
    min_idx = 0

    if len(worst_list) == 0:
        answer.append(-1)
    else:
        for worst in worst_list:
            if scores[worst] <= min_score:
                min_score = scores[worst]
                min_idx = worst
        answer.append(min_idx)

    return answer