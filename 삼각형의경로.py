import copy
def solution(triangle):
    answer = 0
    dp=copy.deepcopy(triangle)
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j]=dp[i][j]+dp[i-1][0]
            elif j == len(triangle[i])-1:
                dp[i][j] = dp[i][j]+dp[i-1][j-1]            
            else:
                dp[i][j] = dp[i][j]+max(dp[i-1][j],dp[i-1][j-1])
    return max(dp[-1])
solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])