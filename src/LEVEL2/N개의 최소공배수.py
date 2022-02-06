import math
def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        # x,y의 최소 공배수 = x*y // x,y의 최대공약수
        answer = i * answer // math.gcd(i, answer)
    return answer