# r 번째 행에 대해서 몇번째 열에 있는 숫자를 고를까?
def backtracking(r, sum):
    global answer
    if sum > answer:
        return

    if r == n:  # 다 고르고 나면 r이 2차원 배열의 크기만큼 되어있다. => 중단조건
        if sum < answer:
            answer = sum
        # 최소합 비교해서 저장

    # 열에 대해서 순회
    for c in range(n):
        # 이 전에 현재 열에 있는 숫자를 고른적이 있는지 검사
        # 전에 골랐던 열이랑 안겹치면 골랐다고 체크
        # 고른 수와 합을 구하고 다음 행으로 이동 (재귀)
        # 함수가 끝나고 나면 다시 돌아옴, 이번 열에 골랏다고 체크한것을 다시 원복
        if ch[c] == 0:
            ch[c] = 1
            backtracking(r + 1, sum + arr[r][c])
            ch[c] = 0

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ch = [0] * n
    answer = 10 * n
    backtracking(0, 0)
    print(f"#{tc} {answer}")