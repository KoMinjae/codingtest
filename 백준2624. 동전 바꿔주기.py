def solution(coindict, coinlist, N):
    dp = list()
    for i in range(len(coinlist)):
        dp.append([0]*(N+1))
        dp[i][0]=1
    total = coinlist[0]
    while coindict[coinlist[0]]!=0:
        dp[0][total]=1
        total+=coinlist[0]
        coindict[coinlist[0]]-=1
    for j in range(1,len(coinlist)):
        coin = coinlist[j]
        for x in range(coindict[coin]+1):
            dp[j][coin*x]+=dp[j-1][0]
            for i in range(1,N):
                num = i + coin*x
                if num <= N:
                    dp[j][num]=dp[j][num]+dp[j-1][i]
                if num > N:
                    break
    return dp[-1][N]

def main():
    N = int(input())
    coindict = dict()
    coinlist = list()
    T = int(input())
    for i in range(T):
        coin, count = map(int,input().split())
        coinlist.append(coin)
        coindict.setdefault(coin,count)
    coinlist.sort()
    if T == 0 or N ==0:
        print(0)
    else:
        print(solution(coindict, coinlist, N))


main()

"""
20
3
5 3
10 2
1 5

"""