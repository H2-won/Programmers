def solution(n, lost, reserve):
    answer = n
    set_r = set(reserve) - set(lost)
    set_l = set(lost) - set(reserve)
    
    for i in set_r:
        if i-1 in set_l:
            set_l.remove(i-1)
        elif i+1 in set_l:
            set_l.remove(i+1)
    return answer - len(set_l)