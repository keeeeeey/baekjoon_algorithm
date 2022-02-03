import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        sum_scoville = first + 2 * second
        heapq.heappush(scoville, sum_scoville)
        answer += 1

    return answer
solution([1, 1, 3, 9, 10, 12], 7)