def solution(msg):
    answer = []
    initlist=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    makedict = dict()
    for i,j in enumerate(initlist):
        makedict[j]=i+1
    idx=0
    addidx=1
    while idx != len(msg):
        if idx+addidx > len(msg):
            abc=msg[idx:idx+addidx+1]
            answer.append(makedict["".join(abc)])
            break
        if "".join(msg[idx:idx+addidx+1]) not in makedict.keys():
            makedict["".join(msg[idx:idx+addidx+1])]=len(makedict)+1
            answer.append(makedict["".join(msg[idx:idx+addidx])])
            idx+=addidx
            addidx=1
        else:
            addidx+=1
    return answer

solution("TOBEORNOTTOBEORTOBEORNOT")