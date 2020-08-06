from collections import Counter
def solution(N, stages):
    answer = []
    members = len(stages)
    falserate= dict()
    stages.sort()
    stagesCounter = (Counter(stages))
    for i in range(0,N):
        if i+1 in stagesCounter:
            falserate[i] = stagesCounter[i+1]/members
            members-=stagesCounter[i+1]
        else:
            falserate[i] = 0
    sortfalse = sorted(falserate.items(), key = lambda x:-x[1])
    answer = [i[0]+1 for i in sortfalse]
    return answer
solution(4, [2,1,3,3,5,1,3,2,4])