from collections import deque
def solution(skill, skill_trees):
    cnt = 0
    for i in skill_trees:
        temp = deque(skill)
        for j in i:
            flag = True
            if j in temp:
                if temp[0] == j:
                    temp.popleft()
                else:
                    flag = False
                    break
        if flag:
            cnt += 1
            
                
    return cnt