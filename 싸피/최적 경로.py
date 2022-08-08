t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    company = (n_list[0], n_list[1])
    home = (n_list[2], n_list[3])
    client_list = []
    visited = [0] * n

    for i in range(4, len(n_list), 2):
        client_list.append((n_list[i], n_list[i + 1]))

    total = 0
    last_client = 0;
    for _ in range(n):
        min_dist = int(1e9)
        for i in range(n):
            if visited[i] == 0:
                dist = abs(company[0] - client_list[i][0]) + abs(company[1] - client_list[i][1])
                if dist < min_dist:
                    min_dist = dist
                    last_client = i
        visited[last_client] = 1
        company = (client_list[last_client][0], client_list[last_client][1])
        total += min_dist
    total += abs(home[0] - client_list[last_client][0]) + abs(home[1] - client_list[last_client][1])
    print(total)