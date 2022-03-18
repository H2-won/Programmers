def compare(begin, target, n):
    cnt = 0
    for i in range(n):
        if begin[i] != target[i]:
            cnt += 1
    return cnt

def dfs(begin, target, words, answer, visited):
    n = len(target)
    if compare(begin, target, n) == 1:
        return answer + 1
    
    for index, i in enumerate(words):
        if visited[index]:
            continue
        if compare(begin, i, n) == 1:
            visited[index] = True
            return dfs(words[index], target, words, answer+1, visited)

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    return dfs(begin, target, words, answer, visited)