def solution(MAPS, N):
    visitied = [[0 for _ in range(N)]for i in range(N)]
    landnum=2
    answer = list()
    mins = 9999
    dx=[1,-1,0,0]; dy =[0,0,1,-1]
    #섬 구분
    for i in range(N):
        for j in range(N):
            if MAPS[i][j] == 1:
                MAPS[i][j] = landnum
                stack = list()
                if visitied[i][j] != 1:
                    visitied[i][j]=1
                    stack.append((i,j))
                    while stack:
                        x, y = stack.pop(0)
                        for k in range(4):
                            mx = x+dx[k]; my = y+dy[k]
                            if 0<=mx<N and 0<=my<N:
                                if MAPS[mx][my]==1:
                                    if visitied[mx][my]==0:
                                        MAPS[mx][my]=landnum
                                        visitied[mx][my]=1
                                        stack.append((mx,my))
                    landnum+=1
    #다리 찾기
    for i in range(N):
        for j in range(N):
            if MAPS[i][j] != 0:
                nowland = MAPS[i][j]
                visitied = [[0 for _ in range(N)]for i in range(N)]
                stack = list()
                if visitied[i][j] != 1:
                    visitied[i][j]=1
                    stack.append((i,j,0))
                    while stack:
                        x, y, count = stack.pop(0)
                        if count > mins:
                            continue
                        for k in range(4):
                            mx = x+dx[k]; my = y+dy[k]
                            if 0<=mx<N and 0<=my<N:
                                if MAPS[mx][my]!=nowland:
                                    if MAPS[mx][my] == 0:
                                        if visitied[mx][my]==0:
                                            visitied[mx][my]=1
                                            stack.append((mx,my,count+1))
                                    elif MAPS[mx][my] != 0:
                                        if mins > count:
                                            mins = count
                                            answer.append(count)
                                        break
    return min(answer)


def main():
    N = int(input())
    MAPS = list()
    for _ in range(N):
        line = list(map(int,input().split()))
        MAPS.append(line)
    print(solution(MAPS,N))
main()