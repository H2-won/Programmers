def solution(N, stages):
    ans = {}
    suc_user_cnt = len(stages)
    for i in range(1, N+1):
        if suc_user_cnt == 0:
            ans[i] = 0
        else:
            stage_fail_cnt = stages.count(i)
            ans[i] = stage_fail_cnt / suc_user_cnt
        suc_user_cnt -= stage_fail_cnt
    # print(ans)
    return sorted(ans, key=lambda x: ans[x], reverse=True)

# ans[x] = 실패율 값이므로, 실패율 값을 기준으로 정렬
