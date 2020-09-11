from collections import deque
def solution(MAPS, L, W):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    answer = list()
    for i in range(L):
        for j in range(W):
            if MAPS[i][j] == "L":
                queue = deque()
                visitied = set()
                queue.append((i,j,0))
                visitied.add((i,j))
                maxlen = 0
                while queue:
                    x, y, count = queue.popleft()
                    if count > maxlen:
                        maxlen=count
                    for k in range(4):
                        mx = x + dx[k]; my = y + dy[k]
                        if 0<=mx<L and 0<=my<W and MAPS[mx][my]=="L":
                            if (mx,my) not in visitied:
                                queue.append((mx,my,count+1))
                                visitied.add((mx,my))
                answer.append(maxlen)
    return max(answer)



def main():
    L, W = map(int,input().split())
    MAPS = list()
    for i in range(L):
        line = list(map(str, list(input())))
        MAPS.append(line)
    print(solution(MAPS, L, W))
main()