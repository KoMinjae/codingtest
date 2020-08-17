from collections import deque

def solution(graph, start):
    visited = list()
    queue = deque()
    queue.append((start,0))
    visited.append(start)
    howlen=list()
    while queue:
        node, count = queue.popleft()
        if node in graph:
            for i in graph[node]:
                if i not in visited:
                    visited.append(i)
                    howlen.append((i,count+1))
                    queue.append((i,count+1))
    howlen.sort(key = lambda x : (-x[1],-x[0]))
    return howlen[0][0]

for test_case in range(1,11):
    N, start = map(int,input().split())
    numlist = list(map(int,input().split()))
    graph={}
    for i in range(0,N,2):
        if numlist[i] not in graph:
            graph[numlist[i]] = [numlist[i+1]]
        else:
            graph[numlist[i]].append(numlist[i+1])

    print('#{} {}'.format(test_case, solution(graph,start)))