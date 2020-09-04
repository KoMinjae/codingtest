def solution(A):
    A.sort()
    dp=[1]*len(A)
    for i in range(1,len(A)):
        for j in range(i):
            if A[i][1] > A[j][1]:
                if dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
    return len(A)-max(dp)


def main():
    N = int(input())
    A=[0]*N
    if N == 1:
        print(0)
    else:
        for i in range(N):
            a,b = map(int,input().split())
            A[i] = (a,b)
        print(solution(A))

main()