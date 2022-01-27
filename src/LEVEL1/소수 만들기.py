from itertools import combinations

def isPrimeNum(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    comList = list(combinations(nums, 3))
    
    for i in comList:
        if isPrimeNum(i[0] + i[1] + i[2]):
            answer += 1
    
    return answer