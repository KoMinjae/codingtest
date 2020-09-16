import math
import heapq as hq
import copy
def solution(graph, start, end):
    godist = list()
    answer = [0]*start
    for i in range(start):
        queue= list()
        dist = [math.inf]*start
        dist[i] = 0
        hq.heappush(queue,[dist[i], i])
        while queue:
            nowvalue, nownode = hq.heappop(queue)
            for nextnode, nextvalue in graph[nownode]:
                if nowvalue+nextvalue <= dist[nextnode]:
                    dist[nextnode]=nowvalue+nextvalue
                    hq.heappush(queue,[dist[nextnode], nextnode])
        if i == end:
            backdist = copy.deepcopy(dist)
        godist.append(dist[end])
    for i in range(start):
        if i != end:
            answer[i] = godist[i]+backdist[i]
    return max(answer)
def main():
    N, M, X = map(int,input().split())
    graph = [[] for _ in range(N)]
    for i in range(M):
        start, end, value = map(int,input().split())
        graph[start-1].append((end-1,value))
    print(solution(graph,N,X-1))

main()