def solution(n, times):
    answer = 0
    times.sort()
    left, right = 0, times[-1] * n
    while left <= right:
        mid = (left+right) // 2
        people = 0
        for i in times:
            people += mid//i
        if people >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer
solution(6,[7,10])

"""SWEA
def main():
    T = int(input())
    for test_case in range(1, T+1):
        N, M = map(int,input().split())
        times=list()
        for i in range(N):
            times.append(int(input()))
        print('#{} {}'.format(test_case, solution(M,times)))
main()
"""