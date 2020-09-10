from collections import deque
def solution(Maps, K, W, H):
    stack = deque()
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    hx=[1,1,-1,-1,2,2,-2,2]
    hy=[2,-2,2,-2,1,-1,1,-1]
    stack.append((0,0,K,0))
    visitied=set()
    visitied.add((0,0,K))
    mins=9999
    while stack:
        x, y, count, answer = stack.popleft()
        if (x,y)==(H-1,W-1):
            return answer
        for j in range(4):
            mx = x+dx[j]; my = y+dy[j]
            if 0<=mx<H and 0<= my < W and (mx,my,count) not in visitied:
                if Maps[mx][my]!=1:
                    stack.append((mx,my,count,answer+1))
                    visitied.add((mx,my,count))
        if count!=0:
            for j in range(8):
                mx = x+hx[j]; my = y+hy[j]
                if 0<=mx<H and 0<= my < W and (mx,my,count-1) not in visitied:
                    if Maps[mx][my]!=1:
                        stack.append((mx,my,count-1,answer+1))
                        visitied.add((mx,my,count-1))
    return -1
    
def main():
    K = int(input())
    W, H = map(int,input().split())
    MAPS = list()
    for i in range(H):
        line = list(map(int,input().split()))
        MAPS.append(line)
    print(solution(MAPS,K,W,H)) 


main()