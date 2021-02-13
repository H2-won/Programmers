def solution(seoul):
    for idx, value in enumerate(seoul):
        if value == 'Kim':
            return '김서방은 %d에 있다' % idx

# def solution(seoul):
#     return '김서방은 %d에 있다'%seoul.index('Kim')

# 리스트.index('string') 함수 알기
