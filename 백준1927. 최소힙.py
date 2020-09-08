import heapq as hq
import sys
queue = list()
hq.heapify(queue)

for i in range(int(input())):
    NUM = int(sys.stdin.readline())
    if NUM == 0:
        if len(queue)==0:
            print(0)
        else:
            print(hq.heappop(queue))
    else:
        hq.heappush(queue,NUM)