from collections import deque
def solution(N,M):
    queue=deque()
    numbers=list()
    queue.append([N,0])
    check={}
    while queue:
        num, cnt = queue.popleft()
        if num == M:
            return cnt
        if check[num]: 
            continue
        check[num] = 1
        for i in range(4):
            if i == 0 :
                if num+1<=1000000:
                    queue.append([num+1,cnt+1])
            elif i == 1 :
                if num-1<=1000000:
                    queue.append([num-1,cnt+1])
            elif i == 2 :
                if num*2<=1000000:
                    queue.append([num*2,cnt+1])
            elif i == 3 :
                if num-10<=1000000:
                    queue.append([num-10,cnt+1])
T=int(input())
for i in range(T):
    a,b = map(int,input().split())
    result=solution(a,b)
    print("#"+str(i+1),result)

