t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    ch = [0] * n
    answer = 0
    for i in range(m):
        for j in range(n):
            if ch[j] == 1:
                continue

            if trucks[i] >= containers[j]:
                answer += containers[j]
                ch[j] = 1
                break

    print(f"#{tc} {answer}")