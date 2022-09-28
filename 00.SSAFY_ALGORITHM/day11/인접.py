'''
마지막 정점번호(0번부터 시작), e 간선수
6 8
0 1 0 2 0 5 0 6 3 4 3 5 6 4 5 4
'''

v, e = map(int, input().split())
info = list(map(int, input().split()))

# 인접행렬
adj_arr = [[0] * (v + 1) for _ in range(v + 1)]
# 인접리스트
adj_list = [[] for _ in range(v + 1)]

for i in range(e):
    a, b = adj_arr[i * 2], adj_arr[i * 2 + 1]
    adj_arr[a][b] = 1
    adj_arr[b][a] = 1

    adj_list[a].append(b)
    adj_list[b].append(a)