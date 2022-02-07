def solution(n):
    oneCnt = bin(n).count('1')
    n+=1
    while bin(n).count('1') != oneCnt:
        n+=1
    return n
  
  # bin(15) = 0b1111 => type은 str, 0b는 2진수라는 뜻