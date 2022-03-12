def dfs(computers, i, visited, n):
        visited[i] = True
        for j in range(n):
            if computers[i][j] and not visited[j]:
                dfs(computers, j, visited, n)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited, n)
            answer += 1
    
    return answer