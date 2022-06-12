def solution(periods, payments, estimates):
    answer = [0, 0]
    for i in range(len(periods)):
        if periods[i] <= 22:
            continue
        elif periods[i] == 23:
            if sum(payments[i][1:12]) + estimates[i] >= 900000:
                answer[0] += 1
        elif 24 <= periods[i] < 59:
            if sum(payments[i]) >= 900000 and sum(payments[i][1:12]) + estimates[i] < 900000:
                answer[1] += 1
            elif sum(payments[i]) < 900000 and sum(payments[i][1:12]) + estimates[i] >= 900000:
                answer[0] += 1
        elif periods[i] == 59:
            if sum(payments[i]) >= 900000 and sum(payments[i][1:12]) + estimates[i] < 600000:
                answer[1] += 1
            elif sum(payments[i]) < 900000 and sum(payments[i][1:12]) + estimates[i] >= 600000:
                answer[0] += 1
        elif periods[i] >= 60:
            if sum(payments[i]) >= 600000 and sum(payments[i][1:12]) + estimates[i] < 600000:
                answer[1] += 1
            elif sum(payments[i]) < 600000 and sum(payments[i][1:12]) + estimates[i] >= 600000:
                answer[0] += 1
    return answer

solution([24, 59, 59, 60], [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [350000, 50000, 40000, 50000])