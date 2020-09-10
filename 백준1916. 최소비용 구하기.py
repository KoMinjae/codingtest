import math
import heapq as hq
def solution(graph,start,end,N):
    dists = [math.inf]*N
    dists[start] = 0
    queue = list()
    hq.heappush(queue,[dists[start],start])
    while queue:
        nowdist, nownode = hq.heappop(queue)
        if graph[nownode]:
            for node, dist in graph[nownode]:
                if nowdist + dist < dists[node]:
                    dists[node] = nowdist+dist
                    hq.heappush(queue,[dists[node], node])

    return dists[end]

def main():
    N = int(input())
    V = int(input())
    graph=[list()for i in range(N)]
    for i in range(V):
        s,e,p = map(int,input().split())
        graph[s-1].append((e-1,p))
    start , end = map(int,input().split())
    print(solution(graph,start-1,end-1,N))

main()