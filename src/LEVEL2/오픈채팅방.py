def solution(record):
    answer = []
    userDict = {}
    for i in record:
        s = i.split()
        if s[0] == 'Enter' or s[0] == 'Change':
            userDict[s[1]] = s[2]
    
    for i in record:
        s = i.split()
        if s[0] == 'Enter':
            answer.append(userDict[s[1]] + '님이 들어왔습니다.')
        elif s[0] == 'Leave':
            answer.append(userDict[s[1]] + '님이 나갔습니다.')
            
    return answer