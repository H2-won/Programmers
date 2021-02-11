def solution(n):
  _three = 0
  i = 0
  while(n >= 3):
    _three += (n % 3) * 10**i
    i += 1
    n //= 3
  _three += n*10**i

  rev = int(str(_three)[::-1])

  _ten = 0
  i = 0
  while(rev > 0):
    _ten += rev % 10 * 3**i
    i += 1
    rev //= 10

  return _ten
