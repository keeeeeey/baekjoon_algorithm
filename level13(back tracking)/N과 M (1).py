N, M = list(map(int, input().split()))
n_list = []

def fn():
    if len(n_list) == M:
        print(" ".join(map(str, n_list)))
        return

    for i in range(1, N + 1):
        if i not in n_list:
            n_list.append(i)
            print(n_list)
            fn()
            n_list.pop()
            print(n_list)
    return

fn()

