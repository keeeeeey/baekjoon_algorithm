t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    answer = [[0, 1, 0]]
    for i in range(n):
        temp = [0]
        for j in range(1, i + 3):
            temp.append(answer[i][j - 1] + answer[i][j])
        temp.append(0)
        answer.append(temp)

    print(f"#{tc}")
    for i in range(n):
        for j in range(1, i + 2):
            print(answer[i][j], end=" ")
        print()
