def adjacent(A_sorted, start, end, l):
    for i in range(start + 1, end):
        s = 0
        e = l - 1
        while s <= e:
            mid = (s + e) // 2
            if A_sorted[mid] > i:
                e = mid - 1
            elif A_sorted[mid] < i:
                s = mid + 1
            else:
                return False
    return True

def solution(A):
    l = len(A)
    A_sorted = sorted(A)
    answer = int(1e9)
    for i in range(l - 1):

        for j in range(i + 1, l):
            flag = True
            if A[i] > A[j]:
                flag = adjacent(A_sorted, A[j], A[i], l)
            elif A[i] < A[j]:
                flag = adjacent(A_sorted, A[i], A[j], l)

            if flag:
                answer = min(answer, abs(A[i] - A[j]))
    return answer

print(solution([0, 3, 7, 5, 11]))

# -- write your code in PostgreSQL 9.4
# SELECT p.name from phones p where p.phone_number = (select c.caller from calls c where 10 <= (select sum(c2.duration) from calls c2 where c2.caller = p.phone_number or c2.callee = p.phone_number))