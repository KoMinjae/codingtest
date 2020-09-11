from collections import deque

def solution(MAPS, N, M):
    move = [(1,0),(-1,0),(0,1),(0,-1)]
    count = 0
    answer = list()
    while True:
        queue = deque()
        queue.append((0,0))
        visitied = set()
        cheese = 0
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                mx,my = x+move[i][0] , y+move[i][1]
                if 0<=mx<N and 0<= my<M:
                    if MAPS[mx][my]==0:
                        if (mx,my) not in visitied:
                            queue.append((mx,my))
                            visitied.add((mx,my))
                    else:
                        MAPS[mx][my]=0
                        visitied.add((mx,my))
                        cheese+=1
        count+=1
        answer.append((count,cheese))
        if cheese==0:
            break
    return answer

def main():
    N, M = map(int,input().split())
    MAPS=list()
    for i in range(N):
        line = list(map(int,input().split()))
        MAPS.append(line)
    answer = solution(MAPS, N, M)
    time = 0
    for i in answer:
        if i[1]==0:
            time = i[0]-1
    print(time)
    print(answer[time-1][1])

main()