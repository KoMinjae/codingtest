def solution(numlist):
    dp = [0]*len(numlist)
    dp[0] = 1
    for i in range(len(numlist)):
        dp[i] = 1
        for j in range(0,i):
            if numlist[i] > numlist[j]:
                dp[i]=max(dp[i], dp[j]+1)
    return max(dp)
def main():
    T=int(input())

    for test_case in range(1, T+1):
        numlist = list(map(int,input().split()))

        print('#{} {}'.format(test_case, solution(numlist)))

main()