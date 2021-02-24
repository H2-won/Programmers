import math


def solution(w, h):
    return w*h - (w+h - math.gcd(w, h))
# 8 12 = 16
# 2 3 = 4
# 4 6 = 8
# 6 8 = 12
# 4 4 = 4
# w+h - gcd(w, h)
