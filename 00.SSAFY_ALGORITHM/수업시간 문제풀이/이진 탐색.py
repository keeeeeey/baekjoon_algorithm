def binary_search(l, r, m):
    global cnt
    left_flag = False
    right_flag = False

    while l <= r:
        mid = (l + r) // 2
        if m > n_list[mid]:
            if right_flag:
                break
            l = mid + 1
            right_flag = True
            left_flag = False
        elif m < n_list[mid]:
            if left_flag:
                break
            r = mid - 1
            left_flag = True
            right_flag = False
        elif m == n_list[mid]:
            cnt += 1
            break

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    n_list = sorted(list(map(int, input().split())))
    m_list = list(map(int, input().split()))
    cnt = 0
    left = 0
    right = n - 1
    for i in range(m):
        binary_search(left, right, m_list[i])
    print(f"#{tc} {cnt}")