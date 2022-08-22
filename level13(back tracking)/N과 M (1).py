N, M = list(map(int, input().split()))
n_list = []

def fn():
    if len(n_list) == M:
        print(" ".join(map(str, n_list)))
        return
    else:
        for i in range(1, N + 1):
            if i not in n_list:
                n_list.append(i)
                fn()
                n_list.pop()

fn()