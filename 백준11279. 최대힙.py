import heapq as hq
import sys
pq = list()

hq.heapify(pq)

for i in range(int(input())):
    N = int(sys.stdin.readline())
    if N == 0:
        if len(pq)==0:
            print(0)
        else:
            print(hq.heappop(pq)*-1)
    else:
        hq.heappush(pq,-N)
