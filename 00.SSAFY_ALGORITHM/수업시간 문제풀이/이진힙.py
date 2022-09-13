def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[c] < heap[p]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def heap_sum(n):
    if n == 0 or n == 1:
        return heap[n]
    else:
        return heap_sum(n // 2) + heap[n]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (n + 1)
    last = 0
    for a in arr:
        enq(a)
    print(f"#{tc} {heap_sum(last // 2)}")
