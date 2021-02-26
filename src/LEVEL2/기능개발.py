def solution(progresses, speeds):
    day = []
    for i in range(len(progresses)):
        cnt = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            cnt += 1
        day.append(cnt)

    answer = []
    d = day.pop(0)
    cnt = 0
    while len(day):
        cnt += 1
        n = day.pop(0)
        if d < n:
            answer.append(cnt)
            cnt = 0
            d = n
    answer.append(cnt+1)

    return answer
