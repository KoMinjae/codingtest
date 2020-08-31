import copy
def solution(MAPS, N, K, highpoint):
    longpath = 0
    stack = list()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visitied = [[0 for _ in range(N)]for _ in range(N)]
    copymap = copy.deepcopy(MAPS)
    for i in highpoint:
        stack.append((i, K, 0, copymap,[i]))
    while stack:
        xy, K, count, nowmap, path = stack.pop()
        if count > longpath:
            longpath=count
        x=xy[0]; y=xy[1]
        for i in range(4):
            newcopymap=copy.deepcopy(nowmap)
            mx = x + dx[i]; my = y + dy[i]
            if mx>=0 and mx<N and my>=0 and my<N:
                if (mx, my) not in path:
                    #깍지 않고 등산 가능한 경우
                    if newcopymap[x][y] > newcopymap[mx][my]:
                        stack.append(((mx,my),K, count+1,newcopymap,path+[(mx,my)]))
                    #깍아서 등산 가능한 경우
                    elif newcopymap[x][y] > newcopymap[mx][my]-K:
                        #K값이 아닌 현 위치 값에서 1만 빼준다
                        newcopymap[mx][my]=newcopymap[x][y]-1
                        if newcopymap[mx][my] <0: newcopymap[mx][my] = 0
                        stack.append(((mx,my),0, count+1,newcopymap,path+[(mx,my)]))
    return longpath+1
def main():
    for test_case in range(1, int(input())+1):
        N, K = map(int,input().split())
        MAPS=list()
        highpoints=list()
        high = 0
        for i in range(N):
            line = list(map(int, input().split()))
            MAPS.append(line)
        for i in range(N):
            for j in range(N):
                if  MAPS[i][j] > high:
                    high = MAPS[i][j]
        for i in range(N):
            for j in range(N):
                if MAPS[i][j] == high:
                    highpoints.append((i,j))
        print("#{} {}".format(test_case, solution(MAPS, N, K, highpoints)))
        
main()