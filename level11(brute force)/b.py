def weight_truck(truck):
    weight = 0
    for w in range(len(truck)):
        weight += truck[w]
    return weight

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = []
    for i in range(len(truck_weights)):
        if truck_weights[i] + weight_truck(truck) <= weight and len(truck) + 1 <= bridge_length:
            truck.append(truck_weights[i])
        
    print(answer)
    return answer

solution(2, 10, [7, 4, 5, 6])