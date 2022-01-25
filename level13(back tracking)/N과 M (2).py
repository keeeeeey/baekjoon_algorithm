N, M = map(int, input().split())
n_list = []
n_list_sort = []

def fn():
    if len(n_list) == M and sorted(n_list) not in n_list_sort:
        print(" ".join(map(str, n_list)))
        n_list_sort.append(sorted(n_list))
        return

    for i in range(1, N + 1):
        if i not in n_list:
            n_list.append(i)
            fn()
            n_list.pop()
    return

fn()