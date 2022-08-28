def dfs(l):
    if l == 3:
        temp = []
        for i in range(3):
            temp.append(ch[i])
        fishing(temp)
    else:
        for i in range(3):
            if ch[i] == -1:
                ch[i] = l
                dfs(l + 1)
                ch[i] = -1

def fishing(temp):
    def positioning(dir, dir2, dist):
        nonlocal position, people, total
        if 0 < dir <= n and position[dir] == 0:
            people -= 1
            total += dist
            position[dir] = 1

        if people <= 0:
            return

        if 0 < dir2 <= n and position[dir2] == 0:
            people -= 1
            total += dist
            position[dir2] = 1

    global answer
    for j in range(2):
        position = [-1] + [0] * n
        total = 0
        for i in range(3):
            gate, people = arr[temp[i]]
            left, right = gate, gate
            dist = 1
            while people > 0:
                if j == 0:
                    positioning(right, left, dist)
                else:
                    positioning(left, right, dist)

                left -= 1
                right += 1
                dist += 1
        answer = min(answer, total)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(3)]

    ch = [-1] * 3
    answer = int(1e9)
    dfs(0)
    print(f"#{tc} {answer}")
