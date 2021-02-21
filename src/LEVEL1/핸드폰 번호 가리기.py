def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number)-4):
        answer += '*'
    return answer + phone_number[-4:]

# 이거 return '*'*(len(phone_number)-4) + phone_number[-4:] 도 가능하다.
# 문자열 곱셈 가능한거 기억하기
