def solution(num, cards):
    answer = 999999
    count=0
    dp=[1000]*(num+1)
    dp[0]=0
    for i in range(1,num+1):
        for j in range(len(cards)):
            if cards[j]<=i:
                dp[i] = min(dp[i], dp[i-cards[j]]+1)
    return dp[-1] if dp[-1] != 1000 else -1

print(solution(18	,[1,2,5]	))