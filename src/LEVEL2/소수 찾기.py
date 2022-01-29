import itertools

def isSosu(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numList = []
    for i in range(len(numbers)):
        per = list(itertools.permutations(numbers, i+1))
        for j in per:
            numList.append(int(''.join(j)))
    print(numList)
    #  입력이 "011" 일 때 numList 출력값 => [0, 1, 1, 1, 1, 10, 11, 10, 11, 11, 11, 101, 110, 101, 110]
    
    for i in set(numList):
        if i >= 2 and isSosu(i):
            answer += 1
                
    return answer