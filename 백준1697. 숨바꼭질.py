from collections import deque
def solution(N,M):
    queue=deque()
    queue.append((N,0))
    visitied=set()
    visitied.add(N)
    while queue:
        x, time = queue.popleft()
        if x == M:
            return time
        for i in range(3):
            if i ==0:
                mx = x*2
                if 0<= mx <=100000:
                    if mx not in visitied:
                        queue.append((mx,time+1))
                        visitied.add(mx)
            elif i == 1:
                mx = x-1
                if 0<= mx <=100000:
                    if mx not in visitied:
                        queue.append((mx,time+1))
                        visitied.add(mx)
            elif i == 2:
                mx = x+1
                if 0<= mx <=100000:
                    if mx not in visitied:
                        queue.append((mx,time+1))
                        visitied.add(mx)


def main():
    N, M = map(int,input().split())

    print(solution(N,M))
main()