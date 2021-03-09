def solution():
    a = input()
    a = a.replace('-', '')
    print(a)
    num = [2, 3, 4, 5, 6, 7, 8, 9]
    sum = 0
    for i in range(12):
        print(int(a[i]), num[i % 8])
        sum += int(a[i]) * num[i % 8]

    print(sum, sum % 11, a[-1])

    if (sum % 11) != a[-1]:
        print('유효하지 않은 주민등록번호입니다.')
    else:
        print('유효한 주민등록번호입니다.')


if __name__ == '__main__':
    solution()
# 821010-1635210
