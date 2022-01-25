import sys
n = int(sys.stdin.readline())

def nqueen(n):
    cnt = 0
    visited = [-1] * n

    def is_ok_on(nth_row):
        for i in range(nth_row):
            if visited[nth_row] == visited[i] or nth_row - i == abs(visited[nth_row] - visited[i]):
                return False
        return True

    def dfs(row):
        if row >= n:
            nonlocal cnt
            cnt += 1
            return

        for col in range(n):
            visited[row] = col
            if is_ok_on(row):
                dfs(row + 1)

    dfs(0)
    print(cnt)
    return cnt

nqueen(n)