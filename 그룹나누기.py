def solution(N,G):
    graph={i:list() for i in range(N)}
    for i in G:
            graph[i[0]-1].append(i[1]-1)
            graph[i[1]-1].append(i[0]-1)
    return 0

solution(5,[[1,2],[3,4]])