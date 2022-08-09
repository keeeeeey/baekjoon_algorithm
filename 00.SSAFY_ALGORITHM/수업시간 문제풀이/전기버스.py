t = int(input())
for tc in range(1, t + 1):
    k, n, m = map(int, input().split()) # k = 정류장 수, n = 종점, m = 충전소 수
    stops = list(map(int, input().split())) # 충전소 위치
    road = [0] * (n + 1)

    for stop in stops: # 충전소 위치 입력
        road[stop] = 1

    answer = 0
    cnt = k
    flag = True

    for i in range(1, n + 1): # 1번 부터 종점까지 순회
        if cnt == 0: # 만약 더이상 가지 못할 경우 flag = False 후 break
            flag = False
            break
        cnt -= 1 # 한칸 전진 후 카운트 차감
        if road[i] == 1: # 만약 현재 위치가 충전소인 경우
            exist = False
            for j in range(1, cnt + 1): # 남은 카운트 수만큼 앞으로 충전소가 있는지 확인
                if road[i + j] == 1 or i + j == n: # 앞에 충전소가 있거나 종점이 있으면 패스
                    exist = True
                    break
            if not exist: # 앞에 충전소나 종점이 없으면 충전 후 충전 횟수 1회 증가
                cnt = k
                answer += 1

    if flag: # 종점까지 도달 했으면 answer 출력
        print(f"#{tc} {answer}")
    else: # 종점까지 도달 못했으면 0 출력
        print(f"#{tc} 0")
