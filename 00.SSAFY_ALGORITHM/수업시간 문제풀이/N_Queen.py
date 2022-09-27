def queen(row):
    global cnt
    if row == n:
        cnt += 1
        return
    else:
        for col in range(n):
            check[row] = col
            if is_ok(row):
                queen(row + 1)

def is_ok(nth_row):
    for i in range(nth_row):
        if check[nth_row] == check[i] or nth_row - i == abs(check[nth_row] - check[i]):
            return False
    return True

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    check = [-1] * n
    cnt = 0
    queen(0)
    print(f"#{tc} {cnt}")