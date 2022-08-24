# 큐 생성
n = 5
q = [0] * n

front = rear = -1

def enQueue(item):  # 큐에 원소를 삽입하는 연산, rear 1씩 증가
    global rear
    # 큐가 만약 꽉 차 있다면 삽입 불가 처리
    # 그게 아니면 rear를 1 증가시키고, 큐에 원소 삽입
    if isFull():
        print("FULL!")
    else:
        rear += 1
        q[rear] = item

def deQueue():      # 큐의 원소를 하나 빼내고 삭제하는 연산, front 1씩 증가
    global front
    # 큐가 만약 비어있다면 삭제 불가 처리
    if isEmpty():
        print("EMPTY!")
    else:
        front += 1
        return q[front]

def isFull():       # 큐가 꽉 찼는지 확인해 주는 함수
    return rear == len(q) - 1

def isEmpty():      # 큐가 비어있는지 확인해 주는 함수 (큐안에 들어잇는 원소 갯수가 0인지)
    return front == rear

for i in range(5):
    enQueue(i)

print(isFull())
enQueue(5)

for i in range(5):
    print(deQueue())

print(isEmpty())
deQueue()