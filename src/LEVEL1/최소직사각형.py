def solution(sizes):
    for i in range(len(sizes)):
        sizes[i].sort()
    return max(i[0] for i in sizes) * max(i[1] for i in sizes)