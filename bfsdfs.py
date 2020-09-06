def bfs_paths(graph, start):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result
def dfs_paths(graph, start):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop()
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result
def main():
    graph={}
    N, M, V = map(int,input().split())
    for i in range(N):
        graph.setdefault(i,[])
    for i in range(M):
        graph[i[0]].append(i[1])
    print(bfs_paths(graph,V),"\n",dfs_paths(graph,V))