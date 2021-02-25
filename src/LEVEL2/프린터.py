from collections import deque


def solution(priorities, location):

    tp = []
    for i, val in enumerate(priorities):
        tp.append((val, i))

    deq = deque(tp)
    cnt = 0

    while len(deq):
        fir = deq.popleft()

        if deq and fir[0] < max(deq)[0]:
            deq.append(fir)
        else:
            cnt += 1
            if fir[1] == location:
                return cnt
