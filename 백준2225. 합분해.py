def solution(N, M):
    dp=list()
    for i in range(M):
        dp.append([0]*(N+1))
    for i in range(N+1):
        dp[0][i]=1
    for i in range(1,M):
        dp[i][0] =1
        for j in range(N+1):
            dp[i][j]=sum(dp[i-1][:j+1]) %1000000000
    return dp[-1][-1]
def main():
    N, M = map(int,input().split())
    if M == 1:
        print(1)
    else:
        print(solution(N,M))

main()