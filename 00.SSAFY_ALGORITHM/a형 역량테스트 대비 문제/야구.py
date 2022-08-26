def dfs():
    pass

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
select = [0 for _ in range(9)]
c = [0 for _ in range(9)]
select[3] = 0
c[3] = 1
ans = 0
dfs(1)
print(ans)