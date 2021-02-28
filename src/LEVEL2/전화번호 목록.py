def solution(phone_book):

    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True

    # startswith, endswith 시작과 끝점 문자열 비교해준다.
