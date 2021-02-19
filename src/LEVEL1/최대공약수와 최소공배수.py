import math


def solution(n, m):
    gcd = math.gcd(n, m)
    return [gcd, n*m] if gcd == 1 else [gcd, n//gcd * m//gcd * gcd]
