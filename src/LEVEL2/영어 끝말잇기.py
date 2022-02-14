def solution(n, words):
    last = words[0][-1]
    for i in range(1, len(words)):           
        if last != words[i][0] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
        last = words[i][-1]
    return [0,0]