def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))

# list는 빼도된다. sorted 하면 list로 알아서 반환되서 나오기 때문이다.
