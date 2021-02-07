# def solution(participant, completion):
#     for i in completion:
#         if i in participant:
#             participant.remove(i)  
#     return participant.pop()

import collections

def solution(participant, completion):
    ans = collections.Counter(participant) - collections.Counter(completion)
    return list(ans)[0]