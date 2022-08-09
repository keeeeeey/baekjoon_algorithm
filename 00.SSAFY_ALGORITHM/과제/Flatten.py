for tc in range(1, 11):
    dump_cnt = int(input())
    boxes = list(map(int, input().split()))
    cnt = 0

    while cnt < dump_cnt:
        cnt += 1
        max_value = 0
        min_value = 100
        max_idx = 0
        min_idx = 0

        for i in range(100):
            if boxes[i] > max_value:
                max_value = boxes[i]
                max_idx = i

            if boxes[i] < min_value:
                min_value = boxes[i]
                min_idx = i

        boxes[min_idx] += 1
        boxes[max_idx] -= 1

    max_answer = 0
    min_answer = 100

    for i in range(100):
        if boxes[i] > max_answer:
            max_answer = boxes[i]

        if boxes[i] < min_answer:
            min_answer = boxes[i]

    print(f"#{tc} {max_answer - min_answer}")