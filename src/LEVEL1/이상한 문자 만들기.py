def solution(s):
    _s = s.split(' ')
    answer = ''
    for word in _s:
        for i, value in enumerate(word):
            if i % 2 == 0:
                answer += value.upper()
            else:
                answer += value.lower()
        answer += ' '
    return answer[:-1]

# 그냥 s.split()을 하면 공백이 여러개인 경우 에러가 난다. split(' ') 으로 사용하기
