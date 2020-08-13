##bfs로 한칸씩 움직이며 해당값을 conut하고 가장 큰 값들을 리턴하자
def solution(maps):
    stack=list()
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    maxnum = 1
    roomnum=9999999
    visited=[[0 for _ in range(len(maps))] for _ in range(len(maps))]
    for j in range(len(maps)):
        for i in range(len(maps[j])):
            if visited[i][j] == 0:
                stack.append((i,j,0))
                while stack:
                    x,y,count = stack.pop(0)
                    visited[x][y] = 1
                    for z in range(4):
                        mx,my = x+dx[z], y+dy[z]
                        if -1<mx<len(maps) and -1<my<len(maps) and maps[x][y] +1 ==maps[mx][my]:
                            x=mx;y=my
                            count+=1
                            stack.append((mx,my,count))
                if count > maxnum:
                    maxnum=count
                    roomnum = maps[i][j]
                elif count == maxnum:
                    if roomnum > maps[i][j]:
                        roomnum = maps[i][j]
    return str(roomnum)+" "+str(maxnum)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    maps = [list(map(int, input().split()))for _ in range(N)]
    print("#"+str(test_case),solution(maps))