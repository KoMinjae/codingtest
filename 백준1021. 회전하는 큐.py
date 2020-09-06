from collections import deque
N, M = map(int,input().split())
queue = deque()
for i in range(N):
    queue.append(i+1)
for i in range(M):
    numlist=list(map(int,input().split()))
count = 0
while count+1!=M:
    num = numlist.pop(0)
    popnum = queue.popleft()
    if popnum == num:
        
    