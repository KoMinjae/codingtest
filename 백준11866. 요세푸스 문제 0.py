N, M = map(int,input().split())
queue = list()

for i in range(N):
    queue.append(i+1)
delindex=list()
idx = M-1
while True:
    delindex.append(str(queue.pop(idx)))
    idx+=M-1
    if not queue:
        break
    while idx >= len(queue):
        idx-=len(queue)
print("<",", ".join(delindex)[:],">", sep='')
