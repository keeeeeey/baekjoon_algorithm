import sys
input = sys.stdin.readline

k, l = map(int, input().split())
success = []
for _ in range(l):
    number = int(input().rstrip())
    if number not in success:
        success.append(number)
    else:
        for i in range(len(success)):
            if success[i] == number:
                del success[i]
                success.append(number)

for i in range(3):
    print(success[i])