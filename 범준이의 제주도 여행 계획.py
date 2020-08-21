def solution(MAPS, nodeinfo, days):
    hotellist = list()
    viewlist = list()
    for i in nodeinfo.items():
        if i[1] == ["A"]:
            Airport = i[0]
        elif i[1] == ["H"]:
            hotellist.append(i[0])
        elif i[1][0] == "P":
            viewlist.append(i[0])
    visited = list()
    stack = list()
    stack.append((Airport,[],0,days,0))
    getroutes = list()
    maxvalue = 0
    while stack:
        position, path, time, day, values = stack.pop(0)
        if day == 0:
            if maxvalue < values:
                maxvalue = values
                getroutes = path
            else :
                continue
        #이동거리는 최소 10분
        if time >530:
            continue
        for i in list(set(range(len(MAPS))).difference(set(path)).union(set(hotellist))):
            if i in viewlist:
                if i not in path :
                    if time+int(MAPS[position][i])+nodeinfo[i][1] > 540:
                        continue
                    stack.append((i,path+[i],time+int(MAPS[position][i])+nodeinfo[i][1],day,values+nodeinfo[i][2]))
            elif i in hotellist:
                if time + int(MAPS[position][i]) > 540:
                    continue
                if day <= 1:
                    continue
                stack.append((i,path+[i],0,day-1,values))
            elif i == Airport:
                if day != 1:
                    continue
                if time + int(MAPS[position][i]) > 540:
                    continue
                stack.append((i,path+[i],time+int(MAPS[position][i]),day-1,values))
    answer = list()
    for i in getroutes:
        answer.append(str(i+1))
    return str(maxvalue)+' '+' '.join(answer)
T= int(input())

for test_case in range(1,T+1):
    N, Day = map(int,input().split())
    info=list()
    infodict=dict()
    MAPS=[[0 for _ in range(N)]for _ in range(N)]
    for i in range(0,N-1):
        route=list(input().split())
        MAPS[i][i]=0
        for j in range(i+1,i+1+len(route)):
            MAPS[i][j]=route[j-i-1]
            MAPS[j][i]=route[j-i-1]
    for i in range(N):
        infos = list(input().split())
        info.append(infos)
    for i in range(len(info)):
        if info[i] == ["A"]:
            infodict[i] = ["A"]
        elif info[i][0] == "P":
            infodict[i] = ["P",int(info[i][1]), int(info[i][2])]
        elif info[i] == ["H"]:
            infodict[i] = ["H"]
    print('#{} {}'.format(test_case, solution(MAPS,infodict,Day)))

