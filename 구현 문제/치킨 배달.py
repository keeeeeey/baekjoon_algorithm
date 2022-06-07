from itertools import combinations

N, M = map(int, input().split())
chicken, house = [], []

for r in range(N):
    N_list = list(map(int, input().split()))
    for c in range(N):
        if N_list[c] == 1:
            house.append((r, c))
        elif N_list[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, M))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)


