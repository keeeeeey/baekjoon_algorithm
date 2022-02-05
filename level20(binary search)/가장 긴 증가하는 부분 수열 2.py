N = int(input())
A = sorted(list(map(int, input().split())))
start = A[0]
end = A[N - 1]
while start <= end:
    mid = (start + end) // 2

