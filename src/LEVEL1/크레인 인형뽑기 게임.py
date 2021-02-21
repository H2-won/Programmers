def solution(board, moves):
    answer = 0
    get = []
    for move in moves:
        for i in board:
            if i[move-1] == 0:
                continue
            elif len(get) > 0 and get[-1] == i[move-1]:
                get.pop()
                answer += 2
            else:
                get.append(i[move-1])
            i[move-1] = 0
            break
    return answer
