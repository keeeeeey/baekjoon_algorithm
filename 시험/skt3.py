def solution(n, plans, clients):
    answer = []
    plan_list = [list(map(int, plan.split())) for plan in plans]
    client_list = [list(map(int, client.split())) for client in clients]
    service = []
    for i in range(len(client_list)):
        for j in range(len(plan_list)):
            flag = True

            for l in range(1, len(plan_list[j])):
                service.append(plan_list[j][l])

            if client_list[i][0] <= plan_list[j][0]:
                for k in range(1, len(client_list[i])):
                    if client_list[i][k] not in service:
                        flag = False
                        break
            else:
                flag = False
            if flag == True:
                answer.append(j + 1)
                break
        if flag == False:
            answer.append(0)

    return answer
