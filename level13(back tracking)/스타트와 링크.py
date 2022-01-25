import sys

T = int(sys.stdin.readline())
N_list = []
for t in range(T):
    N_list.append(list(map(int, sys.stdin.readline().split())))

ans = sys.maxsize
# def div(idx, cnt):
#     if cnt == T // 2:
#         pass
# div(0, 0)
# print(ans)
base_arr = list(range(1, T+1))
comb_arr = []
arr_set = []
def comb(k, c, last):
    if len(c) == k:
        arr_set.append(comb_arr[:])
        return

    for i in range(last, len(base_arr)):
        c.append(base_arr[i])
        comb(k, c, i+1)
        c.pop()

comb(T//2, comb_arr, 0)

def score(l):
    total = 0
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            a = l[i]
            b = l[j]
            total += N_list[a-1][b-1] + N_list[b-1][a-1]
    return total
for arr in arr_set[:len(arr_set) // 2]:
    total_1 = score(arr)
    arr2 = []
    for i in range(1, T+1):
        if i not in arr:
            arr2.append(i)
    total_2 = score(arr2)

    ans = min(ans, abs(total_2-total_1))
print(ans)

