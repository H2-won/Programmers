def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key=len)
    for i in s:
        sList = list(map(int, i.split(",")))
        for j in sList:
            if j not in answer:
                answer.append(j)
    return answer