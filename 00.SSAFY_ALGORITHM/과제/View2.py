for tc in range(1, 11):
    l = int(input())
    buildings = list(map(int, input().split()))
    answer = 0
    i = 2
    while i < l - 2:
        if buildings[i] > buildings[i - 1] and buildings[i] > buildings[i - 2] and buildings[i] > buildings[i + 1] and buildings[i] > buildings[i + 2]:
            max_height = 0
            for j in range(1, 3):
                if buildings[i - j] > max_height:
                    max_height = buildings[i - j]

                if buildings[i + j] > max_height:
                    max_height = buildings[i + j]

            answer += buildings[i] - max_height
            i += 3
        else:
            i += 1

    print(f"#{tc} {answer}")
