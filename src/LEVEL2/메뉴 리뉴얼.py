from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    combiOrder = []
    for i in course:
        combiOrder = []
        for j in orders:
            combiOrder += combinations(sorted(j), i)
        counter = Counter(combiOrder)
        
        if len(counter) and max(counter.values()) >= 2:
            for k, cnt in counter.most_common():
                if cnt == max(counter.values()):
                    answer.append(''.join(k))

    return sorted(answer)