from collections import defaultdict
def solution(gems):
    answer=0
    candidate=[0]
    gemcount = len(set(gems))
    gemslen=len(gems)
    gemdict=defaultdict(int)
    if gemcount==1:
        return [1,1]
    else:
        start = 0
        end = 1
        minlen=987654321
        gemdict[gems[start]]+=1
        gemdict[gems[end]]+=1
        while True:
            if len(gemdict)==gemcount:
                if end-start < minlen:
                    minlen=end-start
                    candidate[0]=[start,end]
                gemdict[gems[start]]-=1
                if gemdict[gems[start]]==0:
                    del(gemdict[gems[start]])
                start+=1
                if start>gemslen-1:
                    break
            else:
                end+=1
                if end > gemslen-1:
                    break
                gemdict[gems[end]]+=1
        return [candidate[0][0]+1,candidate[0][1]+1]

solution(["AA", "AB", "AC", "AA", "AC"])