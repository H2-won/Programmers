import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    for i in range(len(scoville)-1):
        if scoville[0] < K:
            heapq.heappush(scoville, heapq.heappop(
                scoville)+heapq.heappop(scoville)*2)
            cnt += 1
    if min(scoville) < K:
        return -1
    return cnt
