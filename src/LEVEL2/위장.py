def solution(clothes):
    answer = 1
    kind = {i[1]: [] for i in clothes}
    for i in clothes:
        kind[i[1]].append(i[0])
    
    for i in kind:
        answer *= (len(kind[i])+1)
        
    return answer-1