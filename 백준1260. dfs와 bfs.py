def bfs_paths(graph, start, N):
    queue = [start]
    visitied=list()
    visitied.append(start)
    answers=list()
    for i in range(N):
        if i in graph:
            graph[i].sort()
    while queue:
        n = queue.pop(0)
        if graph[n]:
            for i in graph[n]:
                if i not in visitied:
                    queue.append(i)
                    visitied.append(i)
    for i in visitied:
        answers.append(str(i))
    return answers
def dfs_paths(graph, start):
    visited, stack = list(), list()
    stack.append(start)
    answers = list()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack+=sorted(list(set(graph[node])-set(visited)),reverse=True)
                
    for i in visited:
        answers.append(str(i))
    return answers
def main():
    graph={}
    N, M, V = map(int,input().split())
    for i in range(N):
        graph.setdefault(i+1,list())
    for i in range(M):
        snode, enode = map(int,input().split())
        graph[snode].append(enode)
        graph[enode].append(snode)
    for i in range(N):
        if i in graph:
            graph[i].sort(reverse=True)
    print(" ".join(dfs_paths(graph,V)))
    print(" ".join(bfs_paths(graph,V,N)))

main()