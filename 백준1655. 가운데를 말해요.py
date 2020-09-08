import heapq as hq
import sys
queue = list()
hq.heapify(queue)

for i in range(int(input())):
    NUM = int(sys.stdin.readline())
    hq.heappush(queue, NUM)
    print(hq.nsmallest(len(queue)//2,queue))