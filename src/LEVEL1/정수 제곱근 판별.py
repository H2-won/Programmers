import math


def solution(n):
    num = math.sqrt(n)
    if num == int(num):
        return (num+1)**2
    else:
        return -1

# math를 사용하지 않고, n**(1/2) 또는 n**.5를 사용해도 제곱근을 구할 수 있다.
