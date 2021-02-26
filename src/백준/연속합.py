def solution():

    n = int(input())
    numbers = list(map(int, input().split(' ')))

    for i in range(1, n):
        numbers[i] = max(numbers[i], numbers[i-1] + numbers[i])

    print(max(numbers))

    return max(numbers)


if __name__ == '__main__':
    # n = 10
    # numbers = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
    # solution(n, numbers)
    solution()
