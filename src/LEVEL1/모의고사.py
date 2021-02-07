def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    for index, value in enumerate(answers):
        if(s1[index%5] == value):
            cnt[0]+=1
        if(s2[index%8] == value):
            cnt[1]+=1
        if(s3[index%10] == value):
            cnt[2]+=1
    maxCnt = max(cnt)
    ans=[]
    for index, value in enumerate(cnt):
        if(maxCnt == value):
            ans.append(index+1)
    return ans