import datetime

""" def solution(n, t, m, timetable):
    answer = ''
    count=0
    inshuttle=0
    firsttime = datetime.time(9,00)
    popindex=list()
    timetable.sort()
    while count != n:
        for j,i in enumerate(timetable):
            if i[0]!="0":
                cruetime=datetime.time(int(i[0]+i[1]),int(i[3]+i[4]))
            elif i[0]=="0":
                cruetime=datetime.time(int(i[1]),int(i[3]+i[4]))
            if inshuttle < m:
                if cruetime <= firsttime:
                    popindex.append(j)
                    inshuttle+=1
        for i in range(0,len(popindex)):
            timetable.pop(0)
        firsttime=firsttime+datetime.time(0,int(t))
        count+=1

    return answer """
def solution(n, t, m, timetable):
    startbus=540
    nextbus=540
    lasttime = 540+(n*t)
    peoplelist=list()
    for i in timetable:
            hour,minute = i.split(":")
            peoplelist.append(int(hour)*60+int(minute))
    while True:
        inbus=m
        i=0
        if n != 0:
            n-=1
            nextbus=nextbus+t
        while True:
            if inbus>0:
                if nextbus>=peoplelist[i]:
                    peoplelist.pop(0)
                    inbus-1
                else:
                    break
            else:
                


solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])
