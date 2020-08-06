def solution(kim,lee):
    today=0
    lates=0
    answer=list()
    for i in range(len(kim)):
        if kim[i]>lee[i]:
            today+=kim[i]-lee[i]
        else : 
            lates+=lee[i]-kim[i]
        if today>=lates:
            answer.append(today-lates)
            today=today-lates
            lates=0
            today=0
        elif today<lates:
            lates-=today
            today=0
            answer.append(0)
    return answer
kim_toss= list(map(int,input().split()))
lee_toss=list(map(int,input().split()))
solution(kim_toss,lee_toss)