from collections import deque

def bfs(call_dict, start):
    cnt = 0
    q = deque()
    q.append([cnt, start])
    visited = [start]
    last = []
    while q:
        c, now = q.popleft()
        if cnt != c:
            cnt += 1
        if now in call_dict.keys():
            for next in call_dict[now]:
                if next not in visited:
                    q.append([c + 1, next])
                    last.append([c, next])
                    visited.append(next)
    last.sort(key=lambda x: (-x[0], -x[1]))
    return last[0][1]

for tc in range(1, 11):
    length, start = map(int, input().split())
    call_dict = {}
    data = list(map(int, input().split()))
    for i in range(0, length, 2):
        if data[i] in call_dict:
            call_dict[data[i]].append(data[i + 1])
        else:
            call_dict[data[i]] = [data[i + 1]]

    print(f"#{tc} {bfs(call_dict, start)}")
