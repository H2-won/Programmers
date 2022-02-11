def solution(rows, columns, queries):
    answer = []
    numbers =[]
    cnt = 1
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(cnt)
            cnt+=1
        numbers.append(row)
    
    
    for i in queries:
        x1, y1, x2, y2 = i[0]-1, i[1]-1, i[2]-1, i[3]-1
        temp = numbers[x1][y1]
        _min = numbers[x1][y1]
        
        # left
        for j in range(x1, x2):
            numbers[j][y1] = numbers[j+1][y1]
            _min = min(_min, numbers[j+1][y1])
        # bottom
        for j in range(y1, y2):
            numbers[x2][j] = numbers[x2][j+1]
            _min = min(_min, numbers[x2][j+1])
        # right
        for j in range(x2, x1, -1):
            numbers[j][y2] = numbers[j-1][y2]
            _min = min(_min, numbers[j-1][y2])
        # top
        for j in range(y2, y1, -1):
            numbers[x1][j] = numbers[x1][j-1]
            _min = min(_min, numbers[x1][j-1])
            
        numbers[x1][y1+1] = temp
        answer.append(_min)
    return answer