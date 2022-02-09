import sys
input = sys.stdin.readline

N = int(input())
stair = list(int(input()) for _ in range(N))
memo = []
for i in range(2):
    cnt = 0
