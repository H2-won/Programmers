def solution(d, budget):
    for i, val in enumerate(sorted(d)):
        budget -= val
        if budget == 0:
            return i+1
        elif budget < 0:
            return i
    # budget > sum(d) 인 경우 다 되니까 len(d) 리턴
    return len(d)
