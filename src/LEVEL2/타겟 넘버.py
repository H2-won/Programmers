def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(index, num):
        if index == n:
            if num == target:
                nonlocal answer
                answer += 1
            return
        dfs(index+1, num + numbers[index])
        dfs(index+1, num - numbers[index])
        
    dfs(0, 0)
    
    return answer