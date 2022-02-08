def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k]*arr2[k][j]
    return answer
  # numpy를 활용하여 (np.matrix(A)*np.matrix(B)).tolist() 를 리턴하면 답이 나오긴한다.