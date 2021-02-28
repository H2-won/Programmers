def solution(people, limit):
    s = 0
    e = len(people) - 1
    cnt = len(people)
    people = sorted(people, reverse=True)
    while s < e:
        if people[s] + people[e] <= limit:
            e -= 1
            cnt -= 1
        s += 1

    return cnt
