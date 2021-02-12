def solution(a, b):
    _sum = 0
    for i in range(min(a, b), max(a, b)+1):
        _sum += i
    return _sum
