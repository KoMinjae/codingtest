parent=dict()
rank=dict()
graph=dict(list())
def solution(n, network, repair):
    mst = list()
    check=[False]*(n+1)
    check[0]=True
    answer = 0
    repair.sort(key= lambda x:x[2])
    for i in range(len(network)):
        network[i].append(0)
    edges = network+repair
    for node in range(n+1):
        make_set(node)
    for edge in edges:
        node_v, node_u, weight = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)
            answer+=weight
    for i in mst:
        check[i[0]]=True
        check[i[1]]=True
    if False in check:
        return -1 
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


solution(4,	[[1, 2]],	[[2, 3, 10], [3, 1, 12]])