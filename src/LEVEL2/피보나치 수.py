def solution(n):
    answer = []
    for i in range(n+1):
        if i==0:
            answer.append(0)
        elif i==1:
            answer.append(1)
        else:
            answer.append((answer[i-2] + answer[i-1])%1234567)
    
    return answer[-1]