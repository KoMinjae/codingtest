import re
def solution(dartResult):
    dartResult=dartResult.replace("10","z").replace("D","2").replace("S","1").replace("T","3")
    answer = 0
    start="hi"
    score=[]
    dartlist=list()
    p = re.compile("[0-9z][123][*#]?")
    dartlist = list(p.findall(dartResult))
    for i in range(0,3):
        if dartlist[i].find("*") != -1:
            if i==0:
                if dartlist[i][0]=="z":
                    score.append(10 ** int(dartlist[i][1]) * 2)
                else:
                    score.append(int(dartlist[i][0]) ** int(dartlist[i][1]) * 2)
            else:
                if dartlist[i][0]=="z":
                    score[i-1]=score[i-1]*2
                    score.append(10 ** int(dartlist[i][1]) * 2)
                else:
                    score[i-1]=score[i-1]*2
                    score.append(int(dartlist[i][0]) ** int(dartlist[i][1]) * 2)
        elif dartlist[i].find("*") == -1:
            if dartlist[i].find("#")!=-1:
                if dartlist[i][0]=="z":
                    score.append(10 ** int(dartlist[i][1]) * -1)
                else:
                    score.append(int(dartlist[i][0]) ** int(dartlist[i][1])*-1)
            else :
                if dartlist[i][0]=="z":
                    score.append(10 ** int(dartlist[i][1]))
                else:
                    score.append(int(dartlist[i][0]) ** int(dartlist[i][1]))
    return sum(score)

print(solution("1D2S0T"))