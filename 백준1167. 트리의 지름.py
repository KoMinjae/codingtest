import sys
input=sys.stdin.readline

def solution(graph,V):
    stack = list()
    visitied = set()
    stack.append((0,0))
    visitied.add(0)
    maxlen = 0
    maxnode=0
    while stack:
        node, dist = stack.pop()
        if dist > maxlen:
            maxlen = dist
            maxnode = node
        for nodedist in graph[node]:
            if nodedist[0] not in visitied:
                stack.append((nodedist[0],dist+nodedist[1]))
                visitied.add(nodedist[0])
    stack = list()
    visitied = set()
    stack.append((maxnode,0))
    visitied.add(maxnode)
    maxlen = 0
    while stack:
        node, dist = stack.pop()
        if dist > maxlen:
            maxlen = dist
            maxnode = node
        for nodedist in graph[node]:
            if nodedist[0] not in visitied:
                stack.append((nodedist[0],dist+nodedist[1]))
                visitied.add(nodedist[0])

    return maxlen
def main():
    V = int(input())
    graph=dict()
    for i in range(V):
        graph.setdefault(i,list())
    for i in range(V):
        line = list(map(int,input().split()))
        for j in range(1,len(line),2):
            
            if line[j] == -1:
                break
            else:
                graph[line[0]-1].append((line[j]-1,line[j+1]))
                graph[line[j]-1].append((line[0]-1,line[j+1]))
    print(solution(graph,V))

main()