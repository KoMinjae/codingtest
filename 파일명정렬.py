from collections import defaultdict
def divheadnum(files):
    inputlist = files
    headnum=list()
    headlist=list()
    numlist = list()
    for i in range(0,len(inputlist)):
        count=0
        head=""
        num=""
        j=0
        temp=0
        while True:
            if inputlist[i][j].isdigit()==False:
                head+=inputlist[i][j]
                j+=1
            elif inputlist[i][j].isdigit()==True:
                temp=j
                break
        while True:
            if count ==5:
                break
            if temp == len(inputlist[i]):
                break
            if inputlist[i][temp].isdigit()==True:
                num+=inputlist[i][temp]
                count+=1
                temp+=1
            elif inputlist[i][temp].isdigit()==False:
                break
        headnum.append(head+num)
        headlist.append(head.lower())
        numlist.append(num)
    return headnum,headlist,numlist

def solution(files):
    answer = []
    filedict=defaultdict(list)
    headnumfiles,headlist,numlist = divheadnum(files)
    for i in range(0,len(files)):
        filedict[i].append((headlist[i],int(numlist[i])))
    sortfiledict = sorted(filedict.items(), key = lambda x : (x[1][0][0],x[1][0][1]))
    for i in sortfiledict:
        answer.append(files[i[0]])
    return answer

solution(["F-F00000.png","foo010bar020.zip","img123344.png","F-A1","img01.png"])