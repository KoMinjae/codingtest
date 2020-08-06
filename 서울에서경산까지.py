def solution(K, travel):
    answer=0
    dp = [[0 for _ in range(100010)]for _ in range(101)]
    dp[0][travel[0][0]] = travel[0][1]
    dp[0][travel[0][2]] = travel[0][3]
    for i in range(1,len(travel)):
        for j in range(K):
            if dp[i-1][j] == 0:
                continue
            if(j+travel[i][0]<=K):
                dp[i][j+travel[i][0]]=max(dp[i][j+travel[i][0]],dp[i-1][j]+travel[i][1])
                answer=max(answer,dp[i][j+travel[i][0]])
            if (j+travel[i][2]<=K):
                dp[i][j+travel[i][2]]=max(dp[i][j+travel[i][2]],dp[i-1][j]+travel[i][3])
                answer=max(answer,dp[i][j+travel[i][2]])
    return answer
solution(1650,[[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]])