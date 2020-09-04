def solution(N, lines):
    if N == 1:
        return lines[0]
    dp=[0]*N
    dp[0] = lines[0]
    dp[1] = lines[0]+lines[1]
    for i in range(2,N):
        dp[i] = max(lines[i]+lines[i-1]+dp[i-3],lines[i]+dp[i-2],dp[i-1])
    return dp[-1]
def main():
    N = int(input())
    lines=list()
    for i in range(N):
        lines.append(int(input()))
    print(solution(N,lines))

main()