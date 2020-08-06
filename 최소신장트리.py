parent = dict()
rank = dict()
#크루스칼 알고리즘
def solution():
    mst = list()
    # 1. 초기화
    for node in range(N+1):
        make_set(str(node))
    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort(key= lambda x:x[2])
    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        node_v, node_u, weight = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)
    answer =0 
    for i in mst:
        answer+=i[2]
    return answer

def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)
    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    graph={'edges':list(set())}
    N,V =map(int,input().split(" "))
    for i in range(V):
        sn, en, weight = map(int,(input().split(" ")))
        graph['edges'].append((str(sn),str(en),weight))
    
    print("#"+str(test_case),solution())
