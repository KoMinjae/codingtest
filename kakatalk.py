import collections
def solution(record):
    answer = []
    talkrecord=[]
    log=[]
    nickname=collections.defaultdict(list)
    for i in record:
        talkrecord.append(i.split(" "))
    for i in talkrecord:
        if(i[0] == "Enter"):
            log.append([i[1],"님이 들어왔습니다."])
            nickname[i[1]]=i[2]
        elif(i[0] == "Leave"):
            log.append([i[1],"님이 나갔습니다."])
        elif(i[0] == "Change"):
            nickname[i[1]]=i[2]
    
    for i in log:
        answer.append(nickname[i[0]]+i[1])
    print(answer)



solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])