def solution(n, costs):
    answer = 0
    startnum = [0]
    visitland=[]
    cost = list(costs)
    cost.sort(key= lambda x : x[2])
    visitland.append(cost[0][0])
    visitland.append(cost[0][1])
    answer+=cost[0][2]
    cost.pop(0)
    while len(visitland) != n:
        for i in cost:
            if i[0] in visitland or i[1] in visitland:
                if i[0] in visitland and i[1] in visitland:
                    continue
                else :
                    if i[0] not in visitland:
                        visitland.append(i[0])
                    if i[1] not in visitland:
                        visitland.append(i[1])
                    answer+=i[2]
                    break
    return answer

solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])