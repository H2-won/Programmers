def solution(s):
    splited = list(map(int,s.split()))
    return str(min(splited))+' '+str(max(splited))