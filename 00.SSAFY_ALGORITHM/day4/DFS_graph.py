# s : start
# V : 정점 개수
# 1, 2, 3, 4, 5, 6, 7
adj = [
]

def dfs(s, V):
    # 정점의 방문 여부를 알기 위한 배열 선언
    visited = [0] * (V + 1) # 0 번 인덱스는 사용 안함
    stack = [] # size xxx
    now = s
    visited[now] = 1 # 시작 위치는 방문했다라고 체크

    # while len(stack) != 0
    while now != 0: # 현재 위치가 0이 아닐때까지
        # 다음 방문 위치를 방문
        for w in range(1, V + 1): # 1 ~ V 번 정점 방문하기
            # 다음 방문 위치가 있고(1), 해당 방문위치를 방문한 적이 없으면
            if adj[now][w] == 1 and visited[w] == 0:
                # 다음 방문 위치 처리
                # 현재 위치를 스택에 저장
                stack.append(now)
                # 다음 방문 위치를 방문했다고 체크
                visited[w] = 1
                # 현재 위치를 다음 위치로 바꾸고
                now = w
                # 탈출
                break
        else:
            # 다음 방문 위치가 없다. (방문했던 곳만 남거나, 아니면 인접한 곳이 아예 없다.)
            if stack:
                # 지난 정점으로 돌아가기
                now = stack.pop()
            else: # 스택이 비어있다. => 탐색 중지
                break
    return

dfs(1, 7)

