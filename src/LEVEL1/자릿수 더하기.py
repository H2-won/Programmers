def solution(n):
    answer = 0
    while(n):
        answer += n % 10
        n //= 10

    return answer

# return sum([int(i) for i in str(n)]) 도 가능
