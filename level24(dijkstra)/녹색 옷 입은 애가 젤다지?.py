import sys
input = sys.stdin.readline

INF = int(1e9)

while True:
    N = int(input())

    if N == 0:
        break

    grid = list(list(map(int, input().split())) for _ in range(N))

