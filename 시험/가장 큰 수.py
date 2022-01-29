def largestNumber(nums):
    N_list = list(map(str, nums)) # 입력 받은 리스트를 스트링으로 변환
    N_list2 = sorted(N_list, key=lambda x: (str, x*9), reverse=True) # 스트링으로 변환한 리스트를 1. 스트링 2. 9번째 자릿수까지 비교한 후 내림차순정렬
    if N_list2 == ["0"] * len(N_list): # 만약 정렬된 리스트가 길이가 len(nums)인 0으로만 이루어져 있다면 "0"만 리턴 아니면 리스트 값을 전부 조인하여 리턴
        N_list2 = "0"
        return N_list2
    else:
        return "".join(N_list2)

largestNumber([0,0])
