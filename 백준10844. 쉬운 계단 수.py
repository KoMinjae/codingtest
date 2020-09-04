def main():
    N = int(input())
    dp=[[0 for _ in range(10)] for _ in range(101)]

    for i in range(1, 101):
        for j in range(10):
            if i == 1:
                dp[i][j] = 1
            else:
                if 1 <= j <= 8:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j+1]
                elif j == 9:
                    dp[i][j] = dp[i-1][j-11]


    print(sum(dp[N][1:10])%1000000000)

main()