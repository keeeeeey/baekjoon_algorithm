# 0 ~ 9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가
# 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를
# 갖는 경우를 triplet이라고 한다.

# 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin이라고 부를 때
# baby-gin 여부를 판단하는 프로그램을 작성하라

num = 345678 # Baby Gin 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if tri + run == 2:
    print("Baby-Gin")
else:
    print("Lose")