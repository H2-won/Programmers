def solution(s):
    zeroCnt = 0
    transCnt = 0
    while s != '1':
        transCnt += 1
        zeroCnt += s.count('0')
        s = bin(len(s.replace('0', '')))[2:]
        
    return [transCnt, zeroCnt]