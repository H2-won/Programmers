def solution(s):
    if len(s)%2 != 0:
        return False
    
    part = ''
    for i in range(len(s)):
        if len(part) == 0 and s[i] == ')':
            return False
        if s[i] == '(':
            part += s[i]
        else:
            part = part[1:]
        
    return len(part) == 0