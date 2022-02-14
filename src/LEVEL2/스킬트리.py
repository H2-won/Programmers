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
  
  # for-else 문을 사용하게 되면 flag 값을 안써도 된다.
  # for문의 루프가 정상적으로 끝났다면 else 로 들어간다. (break, return 등으로 루프가 끊긴다면 else에 해당되지 않는다.)