t = int(input())
for tc in range(1, t + 1):
    strs = [list(input()) for _ in range(5)]
    max_len = 0
    answer = ""
    for str in strs:
        if len(str) > max_len:
            max_len = len(str)

    for i in range(max_len):
        for str in strs:
            if i < len(str):
                answer += str[i]

    print(f"#{tc} {answer}")