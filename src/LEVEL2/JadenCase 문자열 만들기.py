def solution(s):
    splited = s.split()
    for i in range(len(splited)):
        splited[i] = splited[i].capitalize()
        
    return ' '.join(splited)