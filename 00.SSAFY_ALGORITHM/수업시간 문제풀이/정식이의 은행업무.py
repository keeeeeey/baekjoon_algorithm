def jungsik(l):
    global answer
    if l == 2:
        temp_binary = binary[ch[0]]
        temp_ternary = ternary[ch[1]]
        if binary[ch[0]]:
            binary[ch[0]] = 0
        else:
            binary[ch[0]] = 1

        for i in range(3):
            if temp_ternary == i:
                continue
            ternary[ch[1]] = i
            flag = compare()

            if flag:
                binary[ch[0]] = temp_binary
                ternary[ch[1]] = temp_ternary
                answer = flag
                return

        binary[ch[0]] = temp_binary
        ternary[ch[1]] = temp_ternary
    else:
        length = len(binary)
        if l == 1:
            length = len(ternary)
        for i in range(length):
            ch[l] = i
            jungsik(l + 1)

def compare():
    tmp_binary = change_binary()
    tmp_ternary = change_ternary()
    if tmp_binary == tmp_ternary:
        return tmp_binary
    else:
        return 0

def change_binary():
    tmp_binary = 0
    for i in range(len(binary)):
        tmp_binary += binary[i] * (2 ** (len(binary) - 1 - i))
    return tmp_binary

def change_ternary():
    tmp_ternary = 0
    for i in range(len(ternary)):
        tmp_ternary += ternary[i] * (3 ** (len(ternary) - 1 - i))
    return tmp_ternary

t = int(input())
for tc in range(1, t + 1):
    binary = list(map(int, input()))
    ternary = list(map(int, input()))
    ch = [-1] * 2
    answer = 0
    jungsik(0)
    print(f"#{tc} {answer}")