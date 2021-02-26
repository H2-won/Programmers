def solution(numbers):
    num = [str(i) for i in numbers]
    s_num = sorted(num, reverse=True, key=lambda x: x*3)

    return str(int(''.join(s_num)))

# lambda x : x*3 => 30 34 3 을 303030 343434 333으로 하여 앞자리부터 비교하여 정렬한다.
# str(int()) 이걸 또 해준 이유는 '000' 같은 경우를 '0'으로 바꿔주기 위함이다.
