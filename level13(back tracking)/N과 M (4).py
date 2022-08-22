N, M = map(int, input().split())
n_list = []
def fn():
    if len(n_list) == M:
        print(" ".join(map(str, n_list)))
        return
    else:
        for i in range(1, N + 1):
            if len(n_list) == 0:
                n_list.append(i)
                fn()
                n_list.pop()
            else:
                if n_list[len(n_list) - 1] <= i:
                    n_list.append(i)
                    fn()
                    n_list.pop()

fn()