import heapq
def solution(graph, K, V, E):
    s=[False]*V
    valuelist=[999999]*V
    valuelist[K-1] = 0
    queue = list()
    heapq.heappush(queue, [valuelist[K-1],K-1])
    while queue:
        now_value, now_node = heapq.heappop(queue)
        for node , value in graph[now_node]:
            new_value = now_value+value
            if new_value < valuelist[node]:
                valuelist[node] = new_value
                heapq.heappush(queue,[new_value,node])

    return valuelist

def main():
    V, E = map(int,input().split())
    K = int(input())
    graph=[[]for i in range(V)]
    for i in range(E):
        start, end, value = map(int,input().split())
        graph[start-1].append((end-1,value))

    answer = solution(graph, K, V, E)
    for i in answer:
        if i == 999999:
            print("INF")
        else:
            print(i)

main()