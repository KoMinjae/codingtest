def solution(N,M):
    ##DFS로 2칸 밑 옆을 확인하며 콩심기
    MAPS = [[0 for _ in range(N)]for _ in range(M)]
    dx = [0,2]
    dy = [2,0]
    for i in range(M):
        for j in range(N):
            if MAPS[i][j]==0:
                for x in range(2):
                    if -1<i+dx[x]<M and -1<j+dy[x]<N:
                        MAPS[i+dx[x]][j+dy[x]]=1
    count = 0
    for i in MAPS:
        count += i.count(0)
    return count

def main():
    T = int(input())
    for test_case in range(1,T+1):
        N,M = map(int, input().split())
        print('#{} {}'.format(test_case, solution(N,M)))

main()