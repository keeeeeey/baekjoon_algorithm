def drive(K, N):  # 버스를 운행하는 함수
    # return = 0 : 충전소가 제대로 배치되어 있지 않아서 완주 불가능
    # return > 0 : 충전소가 제대로 배치되어 있다.
    last = 0  # 마지막 충전 위치
    next = K  # 버스가 최대로 이동한 위치(초기값은 한 번 이동한 상태로)
    count = 0  # 충전한 횟수

    # 종점에 도착할 때까지 계속 반복
    while next < N:
        # 버스가 이동한 위치에 충전기가 있나 없나 검사
        # 충전기가 없다면 뒤로 한칸씩 돌아가면서 찾을 때까지 뒤로 간다.
        # 만약 뒤로 갔는데 내가 마지막으로 충전한 위치 까지 와버렸다면
        # 다시 앞으로 가봤자 다시 돌아올테니까 충전소가 제대로 설치되어있지 않을 것이다!
        while stop[next] == 0:
            next -= 1
            if next == last:
                return 0  # 운행 불가

        # 여기까지 왔다면 충전기가 제대로 설치되어 있다.
        # 마지막 충전 위치를 갱신
        last = next
        # 다음 위치로 이동
        next += K
        # 충전횟수 증가
        count += 1
    # N 보다 next 가 크거나 같아졌으니까 완주 했다.
    return count


T = int(input())  # 노선 수

for t in range(1, T + 1):
    # 한번 충전으로 이동할 수 있는 정류장 수, 종점인 정류장(가야 할 거리), 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())
    # 충전기가 설치 되어있는 정류장 번호 리스트
    charge = list(map(int, input().split()))

    stop = [0] * N  # 정류장 리스트(1 : 충전소가 있는 정류장, 0: 충전소가 없는 정류장)
    for i in charge:
        stop[i] = 1  # 충전기가 설치되어 있는 정류장을 1로 표현한 리스트
    answer = drive(K, N)
    print(f'#{t} {answer}')