def solution(numbers, target):
    answer = 0
    cnt = 0
    operator = [len(numbers), 0]
    for i in range(len(numbers)):
        operator[0] -= 1
        operator[1] += 1
        def fn(ans, idx, plus, minus):
            if target == ans and plus == 0 and minus == 0:
                nonlocal cnt
                cnt += 1
                return

            if plus > 0:
                fn(ans + numbers[idx], idx + 1, plus - 1, minus)
            if minus > 0:
                fn(ans - numbers[idx], idx + 1, plus, minus - 1)

        fn(answer, 0, operator[0], operator[1])

    print(cnt)
    return cnt

solution([1, 1, 1, 1, 1], 5)