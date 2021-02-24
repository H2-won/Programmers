import re


def solution(dartResult):
    zone = {
        'S': 1,
        'D': 2,
        'T': 3
    }

    # \d+ = 정수(10이상도 찾음), [SDT] = S/D/T 중에, [*#]? = */# 중에 찾는데 없을수도 있음
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)

    score = []
    for i in dart:
        score.append(int(i[0])**zone[i[1]])
        if i[2] == '#':
            score[-1] *= -1
        elif i[2] == '*':
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2

    return sum(score)

# 정규표현식 알기, import re
