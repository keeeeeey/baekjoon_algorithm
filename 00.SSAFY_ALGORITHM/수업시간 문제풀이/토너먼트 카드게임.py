# 카드게임 분할정복 함수
# i, j : i번째 학생부터 j번째 학생까지
def tournament(i, j):
    if i == j:
        # i랑 j가 같으면 둘로 쪼개는게 불가능 하다.
        return i
    # 왼쪽과 오른쪽을 나누는 일을 계속 반복적으로 하니까
    # 재귀함수로 만들자
    else:
        left = tournament(i, (i + j) // 2) # 왼쪽 쪼개기
        right = tournament((i + j) // 2 + 1, j) # 오른쪽 쪼개기
        return winner(left, right) # left와 right 중 승자를 구해서 리턴

def winner(left, right):
    if rsp[left] == 1 and rsp[right] == 2 or rsp[left] == 2 and rsp[right] == 3 or rsp[left] == 3 and rsp[right] == 1:
        return right
    else:
        return left

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    rsp = list(map(int, input().split()))
    answer = tournament(0, n - 1)
    print(f"#{tc} {answer + 1}")