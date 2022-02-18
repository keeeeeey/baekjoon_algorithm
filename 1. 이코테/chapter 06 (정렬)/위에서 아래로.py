N = int(input())
N_list = list(int(input()) for _ in range(N))
print(" ".join(map(str, sorted(N_list, reverse=True))))