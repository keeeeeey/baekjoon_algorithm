# 최소공배수, 최대공약수, 소수

# - 최소공배수 : 두수에 서로 공통으로 존재하는 배수(공배수) 중 작은수
# - 최대공약수 : 두수에 서로 공통으로 존재하는 약수(공약수) 중 큰수
# - 소수 : 약수가 1 또는 자기 자신밖에 없는 숫자(prime number)

# - 최소공배수를 구하는 방법
# - 최대공약수를 구하는 방법
# - 소수인지 아닌지 판별하는 방법

# 유클리드 호제법
# 2개의 자연수 a, b(a > b) 에 대해서 a를 b로 나눈 나머지가 r일때,
# a와 b의 최대공약수는 b와 r의 최대 공약수와 같다.
# 이 과정을 반복해서 나머지가 0이 되었을때, 이때 나누는 수가 a와 b의 최대공약수이다.

# - 최소공배수의 성질
# 두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수로 나눈것과 같다.

# 최대 공약수 구하기
# gcd : greatest common divisor
def gcd(a, b):
    r = 0 # 나머지
    # a를 나누어 떨어질때까지 나눈다.
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print(gcd(6, 9))

# 최소 공배수 구하기
# lcm : least common multiple
def lcm(a, b):
    return (a * b) // gcd(a, b)

print(lcm(6, 9))

# 소수 구하는 방법(소수인지 확인하는 방법)

# 숫자 n이 숫자이면 True 리턴, 소수가 아니면 False를 리턴하도록
# 소수인지 판별하는 방법은 1부터 n까지 나눴을때 약수가 1 또는 자기 자신밖에 없으면 소수
# 그게 아니면 소수가 아니다.
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(5))
print(is_prime(10))

# 에라토스테네스의 체
# 수학자 에라토스테네스가 고안한 방법. 마체 체로 치듯이 수를 걸러낸다고해서 붙여진 이름이다.
def get_prime(n): # n 까지의 숫자 중에서 소수를 구한다.
    arr = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if arr[i]: # 만약 i번째 수가 소수다
            # 소수의 배수를 모두 소수가 아니라고 체크
            for j in range(i + i, n + 1, i):
                arr[j] = False

    return [i for i in range(2, n + 1) if arr[i] == True]

print(get_prime(100))

# n 까지 다 검사하지 않고, n의 제곱근 까지만 검사해서 최적화

# 제곱근 쓰는 이유??
# n = a*b 로 나타낼 수 있다. n' 를 n의 제곱근이라고 하자.
# n = n' * n' 여기서 a >= n'일때, a*b=n=n'*n' b <= n'
# n' 까지만 검사를 하면 두 수 ab 중에 작은수 b까지만 체크해봐도 (a는 검사를 안해도)
# 소수인지 아닌지 판별이 가능하다.

