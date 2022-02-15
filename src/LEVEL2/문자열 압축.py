def solution(s):
    minLen = len(s)
    for i in range(len(s)//2):
        unit = i+1
        cnt = 1
        trans = ''
        for j in range(unit,len(s)+1,unit):
            now = s[j:j+unit]
            before = s[j-unit:j]
            
            if len(now) < unit:
                if cnt > 1:
                    trans += str(cnt) + before + now
                    cnt = 1
                else:
                    trans += before + now
                continue
                
            if now == before:
                cnt += 1
            else:
                if cnt > 1:
                    trans += str(cnt) + before
                    cnt = 1
                else:
                    trans += before
                    
        minLen = min(minLen, len(trans))

    return minLen