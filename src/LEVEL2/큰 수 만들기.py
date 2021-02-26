def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)
