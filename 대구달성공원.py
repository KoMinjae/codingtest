def solution(N):
    answer = 0
    dp = [0 for i in range(N)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3,N+1):
        dp[i] = dp[i-2] + dp[i-1]
    answer = 2(dp[N]+dp[N-1]) + 2(dp[N-1]+dp[N-2])
    return answer

print(solution(5))