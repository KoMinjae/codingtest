def solution(MAPS,N,M):
    stack=list()
    visitied=list()
    stack.append((0,0,1))
    visitied.append((0,0))
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    answer = list()
    while stack:
        x,y,count = stack.pop(0)
        if (x,y) == (N-1,M-1):
            answer.append(count)
        
        for i in range(4):
            mx = x+dx[i]; my = y + dy[i]
            if 0<=mx<N and 0<=my<M and (mx,my) not in visitied:
                if MAPS[mx][my]==1:
                    stack.append((mx,my,count+1))
                    visitied.append((mx,my))
    return min(answer)
def main():
    N, M = map(int,input().split())
    MAPS = list()
    for i in range(N):
        line = list(map(int,list(input())))
        MAPS.append(line)
    print(solution(MAPS,N,M))

main()