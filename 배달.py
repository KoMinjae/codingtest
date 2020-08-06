import collections
def bfs(route,start,maxcost):
    queue = collections.deque()
    visited=set()
    queue.append([start,[start],0])
    while queue:
        n, path, cost = queue.popleft()
        if cost<=maxcost:
            if path[-1] not in visited:
                visited.add(path[-1])
        if n in route:
            for i in route[n]:
                if i[0] not in path:
                    queue.append([i[0],path+[i[0]],cost+i[1]])
    return visited
def solution(N, road, K):
    graph={i:list() for i in range(1,N+1)}
    for i in road:
        graph[i[0]].append([i[1],i[2]])
        graph[i[1]].append([i[0],i[2]])
    return len(bfs(graph,1,K))
solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2],[5,4,1]],3)