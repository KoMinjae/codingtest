import heapq as hq
def solution(n, works):
    answer = 0
    heap = list()
    for i in works:
        hq.heappush(heap,-i)
    if sum(works)<n:
        return 0
    for i in range(n):
        work = hq.heappop(heap)
        hq.heappush(heap,work+1)
    answer = sum([i*i for i in works])
    return answer

solution(4,[4,3,3])