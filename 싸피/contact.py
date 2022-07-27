def bfs(call_dict, start):
    pass

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
