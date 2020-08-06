def solution(lines):
    answer = list()
    tiles = list()
    times = list()
    protimes = list()
    gettotaltime=list()
    starts=list()
    ends=list()
    duration=list()
    for i in lines:
        date, time, protime = i.split(" ")
        times.append(time)
        protimes.append(protime)
    for i in times:
        gettotaltime.append(gettime(i))
    for i in range(len(gettotaltime)):
        a,b= dividestartend(gettotaltime[i], protimes[i])
        starts.append(a)
        ends.append(b)
        duration.append([a,b])
    answer = max(checktraffic(duration))
    return answer

def gettime(s):
    alltime = s.split(":")
    hour = alltime[0]
    mins = alltime[1]
    sec = alltime[2]
    totalsec = int(hour)*3600 + int(mins)*60 + float(sec)
    return totalsec
def dividestartend(tt,pt):
    pttime=float(pt[:-1])
    starttime=tt-pttime
    endtime=tt
    return round(starttime-0.001,3), endtime
def checktraffic(duras):
    countlist=list()
    for i in duras:
        count =0
        for j in duras:
            if not (j[1]<i[0]or j[0]>=i[1]):    
                count+=1
        countlist.append(count)
    return countlist
solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])