import heapq as hq

def solution(jobs):
    lens=len(jobs)
    answer = 0
    heap = list()
    jobs.sort()
    hq.heappush(heap,jobs.pop(0))
    first = hq.heappop(heap)
    time = first[0]+first[1]
    answer = first[1]
    lasttime=first[0]+first[1]
    deleteindex=list()
    
    while True:
        if jobs:
            for i in range(len(jobs)):
                if jobs[i][0] <= time:
                    hq.heappush(heap,[jobs[i][1],jobs[i][0]])
                    deleteindex.append([jobs[i][1],jobs[i][0]])
                else:
                    break
        for i in deleteindex:
            jobs.pop(jobs.index([i[1],i[0]]))
        deleteindex=list()
        if len(heap)==0:
            time+=1
        else:
            if  lasttime==time:
                temp = hq.heappop(heap)
                answer+=time-temp[1]+temp[0]
                time+=temp[0]
                lasttime=time
            elif lasttime !=time:
                temp = hq.heappop(heap)
                answer+=temp[0]
                time+=temp[0]
                lasttime=time
        if len(jobs)==0 and len(heap)==0:
            break
    x,y = divmod(answer,lens)
    return x

solution(
[[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])