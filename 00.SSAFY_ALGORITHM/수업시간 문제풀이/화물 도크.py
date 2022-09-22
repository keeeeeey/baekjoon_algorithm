t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    containers = [list(map(int, input().split())) for _ in range(n)]
    containers.sort(key=lambda x: x[1])
    answer = 1
    i = 0

    while True:
        flag = False
        for j in range(i + 1, n):
            if containers[i][1] <= containers[j][0]:
                answer += 1
                i = j
                flag = True
                break
        if not flag:
            break
    print(f"#{tc} {answer}")