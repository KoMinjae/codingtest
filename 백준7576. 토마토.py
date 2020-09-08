from collections import deque

def solution(MAPS, N, M):
    tomatoidx=deque()
    for i in range(M):
        for j in range(N):
            if MAPS[i][j] == 1:
                tomatoidx.append((i,j,0))
    dx=[0,0,1,-1]; dy=[1,-1,0,0]
    maxday=0
    while tomatoidx:
        x,y,day = tomatoidx.popleft()
        if maxday<day:
            maxday=day
        for i in range(4):
            mx=x+dx[i]; my=y+dy[i]
            if 0<=mx<M and 0<=my<N and MAPS[mx][my]==0:
                tomatoidx.append((mx,my,day+1))
                MAPS[mx][my]=1
    for i in range(M):
        if 0 in MAPS[i]:
            return -1
    return maxday

def main():
    N, M =map(int,input().split())
    MAPS=list()
    notTomato=True
    notZeroTomato=True
    for i in range(M):
        line = list(map(int,input().split()))
        MAPS.append(line)
    for i in range(M):
        if 0 in MAPS[i]:
            notZeroTomato=False
        if 1 in MAPS[i]:
            notTomato=False
    if notTomato:
        print(-1)
    else:
        if notZeroTomato:
            print(0)
        else:
            print(solution(MAPS,N,M))

main()