def solution(MAPS,bug, N,M):
    stack = list()
    visitied = list()
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    count=0
    for i in range(len(MAPS)):
        for j in range(len(MAPS[i])):
            if MAPS[i][j] == 1:
                stack.append((i,j))
                visitied.append((i,j))
                MAPS[i][j]=2
                count+=1
                while stack:
                    x,y = stack.pop()
                    for m in range(4):
                        mx = x+dx[m]; my=y+dy[m]
                        if 0<=mx<M and 0<=my<N and MAPS[mx][my] == 1:
                            if (mx,my) not in visitied:
                                MAPS[mx][my]=2
                                stack.append((mx,my))
                                visitied.append((mx,my))
    return count
def main():
    for test_case in range(int(input())):
        M, N, K = map(int,input().split())
        MAPS = [[0 for _ in range(N)]for _ in range(M)]
        for i in range(K):
            bugx, bugy = map(int,input().split())
            MAPS[bugx][bugy] = 1
        print(solution(MAPS, K, N, M))

main()