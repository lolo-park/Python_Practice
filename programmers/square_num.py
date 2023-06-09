"""
어떤 자연수를 제곱(2)했을 때 나오는 정수를 제곱수
매개변수 : n
n이 제곱수라면 1 아니라면 2
3의 2제곱 = 9
144가 제곱수인지 아닌지 어떻게 알 수 있나 ?
144 는 12의 제곱
"""
import math

def solution(n):
    for i in range(n):
        if n == math.pow(i, 2):
        # pow(a,b) 는 a의 b제곱을 반환한다
            if i > 0:
                return 1
            elif i.isNull() == True:
                return 2


print(solution(144))  # None 의 이유는 무엇인가


# 다시 접근해야한다.
# 제곱근을 구해내는 문제라는 것을 먼저 캐치했어야했다.
# a ** b 가 a의 b제곱을 구하는 공식이라고 했을 때,
# a ** 1/b 는 a 가 되는 제곱근 b를 구하는 공식이라는 것을 생각해냈으면 쉬웠다.

def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2
# n 이라는 숫자의 제곱근을 구한다 n ** 1/2
# 이게 있는 거라면 (정수라면) 1로 나눈 나머지를 구했을 때 0이 나올 것이다.
# 정수가 아니라면 (소수점자리라면) 0이 될 수 없기때문에 2를 출력하도록 한다.
# 매우 간단 .. !