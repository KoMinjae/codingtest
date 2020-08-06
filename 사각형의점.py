from collections import defaultdict
def solution(v):
    answer = []
    positionxdict=defaultdict(int)
    positionydict=defaultdict(int)
    
    for x,y in v:
        positionxdict[x]=positionxdict[x]+1
        positionydict[y]=positionydict[y]+1
    for x in positionxdict:
        if positionxdict[x]==1:
            answer.append(x)
    for x in positionydict:
        if positionydict[x]==1:
            answer.append(x)

    return answer

solution([[1, 1], [1, 2], [2, 2]])