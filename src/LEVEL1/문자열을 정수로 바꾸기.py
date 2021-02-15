def solution(s):
    if(s[0] == '-'):
        return -int(s[1:len(s)])
    elif(s[0] == '+'):
        return +int(s[1:len(s)])
    else:
        return int(s)

# +, - 또한 int(s)를 통해 인식이 되서 자동으로 처리된다!
