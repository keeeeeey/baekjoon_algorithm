for t in range(1, 11):

    N = int(input())  # 덤프
    heights = list(map(int, input().split()))  # 8 2 3 4 6

    cnt = [0] * 101
    for i in heights:  # 0 0 2 3 4 0 6 0 8
        cnt[i] = cnt[i] + 1  # heights만큼 리스트에 1씩 넣어 층 카운팅

    highest = 0
    lowest = 101

    for height in heights:
        if highest < height:
            highest = height  # 가장 높은 수가 들어감
        if lowest > height:
            lowest = height

    n = 0
    while n < N:  # 5
        cnt[highest] = cnt[highest] - 1
        cnt[highest - 1] = cnt[highest - 1] + 1
        cnt[lowest] = cnt[lowest] - 1
        cnt[lowest + 1] = cnt[lowest + 1] + 1

        if cnt[highest] == 0:
            highest = highest - 1
        if cnt[lowest] == 0:
            lowest = lowest + 1

        n = n + 1
    ans = highest - lowest

    print(f"#{t} {ans}")