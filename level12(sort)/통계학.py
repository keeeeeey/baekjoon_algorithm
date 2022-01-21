import collections
from collections import Counter
import sys

def do_a_avg(N):
    a_sum = 0
    for i in range(len(N)):
        a_sum += N[i]
    a_avg = round(a_sum / len(N))
    return a_avg

def do_middle_num(N):
    return N[len(N) // 2]

def do_count(N):
    count_dict = Counter(N).most_common()
    try:
        if count_dict[0][1] == count_dict[1][1]:
            return count_dict[1][0]
        else:
            return count_dict[0][0]
    except:
        return count_dict[0][0]

def do_max_min(N):
    max_num = max(N)
    min_num = min(N)
    return max_num - min_num

T = int(input())
N = [int(sys.stdin.readline()) for _ in range(T)]
N.sort()
print(do_a_avg(N))
print(do_middle_num(N))
print(do_count(N))
print(do_max_min(N))



