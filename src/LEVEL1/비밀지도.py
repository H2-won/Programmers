def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        cnt = n - 1
        ans = [' ']*n
        while arr1[i] > 0 or arr2[i] > 0:
            if arr1[i] % 2 == 1 or arr2[i] % 2 == 1:
                ans[cnt] = '#'
            arr1[i] //= 2
            arr2[i] //= 2
            cnt -= 1
        answer.append(''.join(ans))

    return answer
