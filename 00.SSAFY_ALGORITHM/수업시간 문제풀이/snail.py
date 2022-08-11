# 홀수인 자연수 n을 입력받는다.
n = int(input())
array = [[0]*n for _ in range(n)]

# 나중에 좌표를 찾을 숫자를 입력받는다.
k = int(input())

# 처음 시작 위치는 0 번째, value값은 n*n 에서 시작한다.
ci = 0
cj = 0
value = n*n

# 하, 우, 상, 왼 순으로 움직인다.
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]



# 첫번째 array 값에 value를 먼저 넣고 시작한다.
array[ci][cj] = value
d = 0
while value > 1:
    for i in range(4):
        d = (d + i) % 4
        ni = ci+di[d]
        nj = cj+dj[d]

        # d 의 방향 바꾸기를 종료하는 조건
        if 0 <= ni < n and 0 <= nj < n and array[ni][nj] == 0:
            ci = ni
            cj = nj
            break;

    value -= 1
    array[ci][cj] = value

for i in range(n):
    for j in range(n):
        print(array[i][j], end=" ")
    print()