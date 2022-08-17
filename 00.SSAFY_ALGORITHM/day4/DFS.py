# DFS(깊이우선탐색)
# 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면
# 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아 와서 다른 방향의 정점으로 탐색을 계속 반복하여
# 결국 모든 정점을 방문하는 순회방법

# 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

# DFS 탐색 방법
# 1. 시작 정점 v를 결정하여 방문한다.
# 2. 정점 v에 인접한 정점 중에서
#   1) 반문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2.를 반복한다.
#   2) 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2.를 반복한다.

# 스택이 공백이 될때까지 2.를 반복한다.

# visited[], stack[] 초기화
# 초기상태 : 배열 visited를 False로 초기화하고, 공백 스택을 생성

adjList = [[1, 2],      # 0
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]]         # 6

def dfs(v, N):
    visited = [0] * N   # visited 생성
    stack = [0] * N     # stack 생성
    top = -1
    print(v)

    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjList[v]:            # if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1                # push(v)
                stack[top] = v
                v = w                   # v <- w
                print(v)
                visited[w] = 1          # visited[w] <- True
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break
dfs(1, 7)






def dfs(v):
    print(v)
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N
dfs(0)