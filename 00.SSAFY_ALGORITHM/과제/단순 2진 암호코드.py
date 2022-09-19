t = int(input())
dict = {
        "0001101" : 0,
        "0011001" : 1,
        "0010011" : 2,
        "0111101" : 3,
        "0100011" : 4,
        "0110001" : 5,
        "0101111" : 6,
        "0111011" : 7,
        "0110111" : 8,
        "0001011" : 9
    }
for tc in range(1, 1 + t):
    n, m = map(int, input().split())
    codes = [list(map(int, input())) for _ in range(n)]
    end_i = 0
    end_j = 0
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if codes[i][j] == 1:
                end_i = i
                end_j = j
                break
    password = []
    for i in range(end_j - 55, end_j + 1, 7):
        code = ""
        for j in range(i, i + 7):
            code += str(codes[end_i][j])
        password.append(dict[code])

    odd = 0
    even = 0
    for i in range(8):
        if i % 2 == 0:
            odd += password[i]
        else:
            even += password[i]

    result = odd * 3 + even
    if result % 10 == 0:
        print(f"#{tc} {sum(password)}")
    else:
        print(f"#{tc} 0")

