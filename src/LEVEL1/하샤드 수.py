def solution(x):
    _x = str(x)
    sum = 0
    for i in _x:
        sum += int(i)
    return x % sum == 0
