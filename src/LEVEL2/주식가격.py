from collections import deque


def solution(prices):
    answer = [0]*len(prices)
    deq = deque(prices)
    cnt = 0
    while len(deq):
        fir = deq.popleft()
        for i in deq:
            answer[cnt] += 1
            if fir > i:
                break
        cnt += 1
    return answer
#     while len(prices):
#         cnt = 0
#         p = prices.pop(0)
#         for i in prices:
#             cnt+=1
#             if p > i:
#                 break
#         answer.append(cnt)
#     return answer

#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         for j in prices[i+1:]:
#             cnt += 1
#             if prices[i] > j:
#                 break
#         answer.append(cnt)
#     return answer
