def solution(N, number):
    answer = 0
    dp = [{}] # dp 순회 index를 1부터 시작
    if N == number:
        return 1
    
    for i in range(1, 9):
        temp = set()
        # 5, 55, 555, 5555 형식의 숫자 추가
        temp.add(int(str(N)*i))
        
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    temp.add(a+b)
                    if a-b > 0: # 뺄셈에서 발생하는 음수를 제거해주면 시간이 확실히 줄어든다.
                        temp.add(a-b)
                    temp.add(a*b)
                    if b != 0:
                        temp.add(a//b)
        if number in temp:
            return i
        dp.append(temp)
        
    return -1