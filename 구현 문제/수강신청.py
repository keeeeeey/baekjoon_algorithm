import sys
input = sys.stdin.readline

k, l = map(int, input().split())
success = {}
for i in range(l):
    student_num = input().rstrip()
    success[student_num] = i

success = sorted(success.items(), key=lambda x: x[1])

if k > len(success):
    k = len(success)

for j in range(k):
    print(success[j][0])