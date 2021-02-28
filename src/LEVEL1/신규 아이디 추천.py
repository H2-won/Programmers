import re


def solution(new_id):
    new_id = new_id.lower()
    # a-z, 0-9, -, _, . 가 아닌 것은 제거
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    # +를 붙여서 하나 이상의 .을 하나의 .으로 치환
    new_id = re.sub('\.+', '.', new_id)
    # (^~~) 시작 또는 (~~&) 끝에 있는 .을 제거
    new_id = re.sub('^\.|\.$', '', new_id)
    new_id = 'a' if len(new_id) == 0 else new_id
    new_id = new_id[:15] if len(new_id) >= 16 else new_id
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id
