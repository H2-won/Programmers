def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    
    # 첫 방향이 아래이고, 0,0부터 넣어야되니까 x=-1에서 시작
    x = -1
    y = 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i%3 == 0: # 아래로
                x+=1
            elif i%3 == 1: # 오른쪽으로
                y+=1
            else: # 왼쪽 위로 
                x-=1
                y-=1
            answer[x][y] = num
            num += 1
            
    return sum(answer, [])