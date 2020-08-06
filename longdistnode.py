from collections import deque
def solution(n, edge):
    graph = [[] for i in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    queue = deque()
    visited=set()
    queue.append(1)
    visited.add(1)
    distance=[0 for i in range(n+1)]
    while queue:
        node = queue.popleft()
        for j in graph[node]:
            if j not in visited:
                visited.add(j)
                queue.append(j)
                distance[j] = distance[node]+1
    answer = distance.count(max(distance))
    return answer

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])