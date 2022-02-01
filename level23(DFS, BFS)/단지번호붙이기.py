T = int(input())
N_list = [list(map(str, input())) for _ in range(T)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
nums = []

def dfs_recursive(r, c):
    if r < 0 or r >= T or c < 0 or c >= T:
        return False

    if N_list[r][c] == '1':
        global count
        count += 1
        N_list[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return True
    return False

cnt = 0
count = 0

for r in range(T):
    for c in range(T):
        if dfs_recursive(r, c) == True:
            nums.append(count)
            cnt += 1
            count = 0

nums.sort()
print(cnt)
for i in range(len(nums)):
    print(nums[i])