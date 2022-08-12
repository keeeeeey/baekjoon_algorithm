def get_prime():
    arr = [True] * (1000)

    m = int(999 ** 0.5)
    for i in range(2, m + 1):
        if arr[i]:
            for j in range(i + i, 1000, i):
                arr[j] = False

    return [i for i in range(7, 1000) if arr[i] == True]

prime_number_list = get_prime()

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    l = len(prime_number_list)
    answer = 0
    subset = []

    def dfs():
        global answer
        if len(subset) == 3:
            print(subset)
            subset_sum = 0
            for prime in subset:
                subset_sum += prime
            if subset_sum == n:
                answer += 1
            return

        for i in range(l):
            subset.append(prime_number_list[i])
            dfs()
            subset.pop()

    dfs()

    print(f"#{tc} {answer}")
