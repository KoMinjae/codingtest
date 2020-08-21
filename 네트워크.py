def solution(n, computers):
    answer = 0
    queue = []
    visited = [0]*n

    while 0 in visited:
        queue.append(visited.index(0))
        while queue:
            node = queue.pop(0)
            visited[node] = 1
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    queue.append(i)
        answer += 1
    return answer
solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
"""
from collections import defaultdict
def solution(n, computers):
    graph=dict()
    lens = len(computers)
    #
    if lens ==1:
        return 1
    for i in range(lens):
        graph[i] = list()
    #
    
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i != j:
                if computers[i][j] == 1:
                    graph[i].append(j)
    visited=list()
    nodes=list()
    for i in range(lens):
        nodes.append(i)
    stack=list()
    stack.append(0)
    visited.append(0)
    nodes.remove(0)
    count=0
    while len(visited) != lens:
        if not stack:
            stack.append(nodes[0])
            visited.append(nodes[0])
            nodes.remove(nodes[0])
        while stack:
            node = stack.pop(0)
            if node in graph:
                for i in graph[node]:
                    if i not in visited:
                        stack.append(i)
                        visited.append(i)
                        nodes.remove(i)
        count+=1
    return count
    

print(solution(3,[1]))
"""