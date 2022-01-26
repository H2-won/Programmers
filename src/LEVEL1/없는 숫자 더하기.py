def solution(numbers):
    answer = 0
    oneToNine = [1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in oneToNine:
            oneToNine.remove(i)
    return sum(oneToNine)