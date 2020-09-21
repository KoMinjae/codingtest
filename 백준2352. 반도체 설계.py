import sys
def solution(nums,N):
    dp = [1] * N
    for i in range(1,N):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

def main():
    N = int(input())
    nums = list(map(int,sys.stdin.readline().split()))
    print(solution(nums,N))

main()