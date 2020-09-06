def solution(graph,start):
    stack = list()
    visitied = list()
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visitied:
            visitied.append(node)
            stack+=list(set(graph[node])-set(visitied))
    return len(visitied)-1

def main():
    N = int(input())
    V = int(input())
    graph={}
    for i in range(V):
        S,E = map(int,input().split())
        graph.setdefault(S,[])
        graph.setdefault(E,[])
        graph[S].append(E)
        graph[E].append(S)
    print(solution(graph,1))

main()

