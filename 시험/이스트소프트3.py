def solution(record):
    answer = [[]]
    for i in range(len(record)):
        p_list = list(map(str, record[i].split()))
        if p_list[1] == "sit":

        elif p_list[1] == "leave":

    return answer

solution(["id=1 sit k=1","id=2 sit k=3","id=3 sit k=2","id=2 leave","id=4 sit k=4","id=5 sit k=2"])