def solution(lottos, win_nums):
    ranks = [6,6,5,4,3,2,1]
    wcnt = 0
    zcnt = 0
    for i in lottos:
        if i == 0:
            zcnt+=1
        elif i in win_nums:
                wcnt+=1  
    
    return [ranks[zcnt+wcnt], ranks[wcnt]]