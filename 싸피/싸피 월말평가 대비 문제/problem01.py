def max_score(scores):
    ans = 0
    for score in scores:
        if score > ans :
            ans = score
    return ans


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
