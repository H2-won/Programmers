def solution(numbers, hand):
    answer = ''
    l_n = 10
    r_n = 12
    for i in numbers:
        if i in [1, 4, 7]:
            l_n = i
            answer += 'L'
        elif i in [3, 6, 9]:
            r_n = i
            answer += 'R'
        else:
            if i == 0:
                i = 11
            if sum(divmod(abs(i-l_n), 3)) < sum(divmod(abs(i-r_n), 3)):
                l_n = i
                answer += 'L'
            elif sum(divmod(abs(i-l_n), 3)) == sum(divmod(abs(i-r_n), 3)):
                if hand == 'left':
                    l_n = i
                    answer += 'L'
                else:
                    r_n = i
                    answer += 'R'
            else:
                r_n = i
                answer += 'R'

    return answer

# 키패드에서 5와 1 거리는 |1-5| 를 3으로 나눈 몫과 나머지의 합임을 이용해서 풀음
