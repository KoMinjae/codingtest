def solution(N, numlist):
    if N == 1:
        return 1
    else:
        dp=[1]*N
        dp[0]=1
        for i in range(1,N):
            for j in range(i):
                if numlist[i] > numlist[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j]+1
        return max(dp) 

def main():
    N=int(input())
    numlist = list(map(int,input().split()))
    print(solution(N,numlist))

main()