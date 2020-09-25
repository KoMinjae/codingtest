from collections import deque
def solution(N, M, MAPS, K):
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    stack = deque()
    stack.append((0,0,0,K))
    visitied=set()
    visitied.add((0,0,K))
    while stack:
        x, y, count, k = stack.popleft()
        if (x,y) == (N-1,M-1):
            return count+1
        for i in range(4):
            mx = x+move[i][0] ; my = y+move[i][1]
            if 0<=mx<N and 0<=my<M:
                if MAPS[mx][my] ==0:
                    if (mx,my,k) not in visitied:
                        stack.append((mx,my,count+1,k))
                        visitied.add((mx,my,k))
                else:
                    if k!=0:
                        if (mx,my,k-1) not in visitied:
                            stack.append((mx,my,count+1,k-1))
                            visitied.add((mx,my,k-1))
    return -1
def main():
    N, M, K = map(int,input().split())
    MAPS= list()
    for i in range(N):
        line = list(map(int,list(input())))
        MAPS.append(line)

    print(solution(N,M,MAPS,K))


main()