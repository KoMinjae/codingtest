def solution(graph,N):
    stack=list()
    maxcountlist=list()
    for i in range(1,N+1):
        stack.append((i,[i]))
        maxcount=0
        while stack:
            node, path = stack.pop()
            if maxcount<len(path):
                maxcount = len(path)
            if node in graph:
                for i in graph[node]:
                    if i not in path:
                        stack.append((i,path+[i]))
        maxcountlist.append(maxcount)
            
    return max(maxcountlist)
def main():
    T = int(input())
    for test_case in range(1,T+1):
        N, M = map(int,input().split())
        graph={}
        if M == 0:
            print("#{} {}".format(test_case, 1))
        else:
            for i in range(M):
                node1, node2 = map(int,input().split())
                graph.setdefault(node1,set())
                graph.setdefault(node2,set())
                graph[node1].add(node2)
                graph[node2].add(node1)
        
            print("#{} {}".format(test_case, solution(graph,N)))

main()
