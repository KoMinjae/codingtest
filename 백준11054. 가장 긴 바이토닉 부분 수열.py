def solution(N, lines):
    if N == 1 :
        return 1
    else:
        dp=[0]*N
        updp=[1]*N
        downdp=[1]*N
        for i in range(N):
            for j in range(i):
                if lines[i] > lines[j]:
                    if updp[i] < updp[j] + 1:
                        updp[i] = updp[j]+1
        for i in range(N-1,0,-1):
            for j in range(N-1,i,-1):
                if lines[i] > lines[j]:
                    if downdp[i] < downdp[j]+1:
                        downdp[i] = downdp[j]+1
        for i in range(N):
            dp[i] = updp[i]+downdp[i]-1
    return max(dp)
def main():
    N = int(input())
    numlist = list(map(int,input().split()))
    print(solution(N,numlist))

main()