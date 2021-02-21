def solution(N, stages):
    ans = {}
    # 1 스테이지부터 시작하니까 도달한 유저 카운트 초기값 len(stages)
    dodal_user_cnt = len(stages)
    for i in range(1, N+1):
        if dodal_user_cnt == 0:
            ans[i] = 0
        else:
            stage_fail_cnt = stages.count(i)
            ans[i] = stage_fail_cnt / dodal_user_cnt
        dodal_user_cnt -= stage_fail_cnt

    return sorted(ans, key=lambda x: ans[x], reverse=True)

# ans[x] = 실패율 값이므로, 실패율 값을 기준으로 정렬
