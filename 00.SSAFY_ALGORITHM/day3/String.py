# 이 전까지는 각 지역별로 코드체계를 정해놓고 사용했지만 인터넷이 발전하면서 지역간에 정보를 주고 받을때
# 정보를 다르게 해석한다는 문제점이 생김

# 그래서 혼동을 피하기 위해 미국에서 ASCII라는 인코딩 표준이 제정됨

# ASCII는 7bit 인코딩으로 128문자를 표현하며 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의
# 출력 가능한 문자들로 이루어져 있다.

# 확장 아스키는 표준 문지 외에 악센트 문자, 도형 문자, 특수 문자, 특수 기호등 부가적인 문잘르 128개 추가할 수 있게 하는 부호
# 표준 아스키는 7bit를 사용하지만 확장 아스키는 1byte(8bit)를 모두 사용한다.

# 확장 아스키는 표준 아스키와는 달리 전세계적으로 통용되지는 않는다.
# 프로그램이나 컴퓨터 또는 프린터가 그것을 해독할 수 있도록 설계되어 있어야 한다.

# 각 나라 별로 자국의 문자 코드체계를 만들어서 사용하고 있으며 우리나라는 조합형과 완성형 두 종류를 가지고 있다.
# 이렇게 각 나라 별로 코드체계를 만들어서 사용하다 보니 국가간 정보를 주고 받을때 문제가 발생했다.
# 그래서 국가간 다국어 처리를 위해 표준을 마련했고 이를 유니코드라고 한다.

# 바이트 순서
# big-endian
# little-endian(intel)

# 유니코드 인코딩(UTF : Unicode Transformation Format)
# UTF-8 (in web)
# - MIN : 8bit, MAX : 32bit(1 Byte * 4)
# UTF-16 (in windows, java)
# - MIN : 16bit, MAX : 32bit(2 Byte * 2)
# UTF-32 (in unix)
# - MIN : 32bit, MAX : 32bit(4 Byte * 1)

def strlen(a):
    idx = 0
    while a[idx] != "\0":
        idx += 1
    return idx

a = ["a", "b", "c", "\0"]
print(strlen(a))

# Java(객체지향 언어)에서의 문자열 처리
# 문자열 데잍를 저장, 처리해주는 클래스를 제공
# String 클래스를 사용한다.
# String 클래스 메소드
# +, length(), replace(), split(), substring(),...
# 보다 풍부한 연산을 제공

# Python에서의 문자열 처리
# char 타입 없음
# 텍스트 데이터의 취급방법이 통일되어 있음
# 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수잇는 인덱싱, 슬라이싱 연산들을 사용할 수 있음
# String 클래스 메소드
# replace(), split(), isalpha(), find()
# immutable

# C와 Java의 String 처리의 기본적인 차이점
# c는 아스키 코드로 저장한다.
# java는 유니코드(UTF16, 2byte)로 저장한다.
# 파이썬은 유니코드(UTF8)로 저장

# 문자열 뒤집기
def my_reverse(s):
    answer = ""
    for i in range(len(s) - 1, -1, -1):
        answer += s[i]
    return answer

def my_reverse_self(s):
    s = list(s)
    for i in range(len(s) // 2):
        s[i], s[-i-1] = s[-i-1], s[i]
    return "".join(s)

print(my_reverse("Reverse this strings"))
print(my_reverse_self("Reverse this strings"))

# 문자열 비교
# c strcmp() 함수를 제공한다.
# Java에서는 equals() 메소드를 제공한다.
# 문자열 비교에서 == 연산은 메모리 참조가 같은지를 묻는 것!!
# 파이썬에서는 == 연산자와 is 연산자를 제공한다.
# == 연산자는 내부적으로 특수 메서드 _eq_()를 호출
s1 = "abc"
s2 = "abc"
s3 = "def"
s4 = s1
s5 = s1[:2] + "c"
print(s1 == s2)
print(s1 == s4)
print(s1 == s5)
print(s1 is s2)
print(s1 is s4)
print(s1 is s5)

# 자바는 == 동일성, equals() 동등성
# 파이썬은 == 동등성, is 동일성

def my_strcmp_pythonic(str1, str2):
    if str1 > str2:
        return -1
    elif str1 < str2:
        return 1
    else:
        return 0

def my_strcmp(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            break
    return ord(str1[i]) - ord(str2[i])
print(my_strcmp("abede", "abcde"))

# 문자열 숫자를 정수로 변환하기
# c 언어에서는 atoi()함수를 제공한다. 역 함수로는 itoa()가 있다.
# java에서는 숫자 클래스의 parse 메소드를 제공한다.
# Integer.parseInt(String)
# 역함수로는 toString() 메소드를 제공한다.

# 파이썬에서는 숫자와 문자변환 함수를 제공한다.
# ex) int(), float(), str(), repr()

def atoi(s):
    i = 0
    for x in s:
        i = i * 10 + ord(x) - ord("0")
    return i

print(atoi("123") + 1)

def itoa(a):
    i = 10
    s = ""
    while a > 0:
        mod = a % i
        s += chr(ord("0") + mod)
        a //= 10
    return s[::-1]

print(itoa(123))

# 패턴 매칭
# 패턴 매칭에 사용되는 알고리즘들
# 고지식한 패턴 검색 알고리즘
# 카프-라빈 알고리즘
# KMP 알고리즘
# 보이어-무어 알고리즘

p = "is" # 찾을 패턴
t = "this is a book~!" # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M # 검색 성공
    else:
        return -1 # 검색 실패

print(BruteForce(p, t))