T = int(input())
score = list(map(int, input().split(" ")))
max_score = max(score)
sum = 0
for i in range(T):
    score[i] = score[i] / max_score * 100
for j in range(T):
    sum += score[j]
avg = sum / T
print(avg)