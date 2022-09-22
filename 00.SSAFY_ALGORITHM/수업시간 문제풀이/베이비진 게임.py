def babyjin(player):
    arr = [0] * 12
    for i in range(len(player)):
        arr[player[i]] += 1

    for i in range(10):
        if arr[i] >= 3:
            return True
        if arr[i] != 0 and arr[i + 1] != 0 and arr[i + 2] != 0:
            return True

    return False


t = int(input())
for tc in range(1, t + 1):
    player1 = []
    player2 = []
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(12):
        if i % 2 == 0:
            player1.append(arr[i])
            if i >= 4:
                flag = babyjin(player1)
                if flag:
                    answer = 1
                    break
        else:
            player2.append(arr[i])
            if i >= 5:
                flag = babyjin(player2)
                if flag:
                    answer = 2
                    break
    print(f"#{tc} {answer}")