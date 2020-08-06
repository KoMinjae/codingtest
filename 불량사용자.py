from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    candidates=set()
    count=0
    if len(user_id)==len(banned_id):
        return 1
    for i in permutations(user_id,len(banned_id)):
        count=0
        for idx in range(len(banned_id)):
            if len(i[idx])!=len(banned_id[idx]):
                break
            else:
                if check(i[idx],banned_id[idx]) ==  False:
                    break
                else :
                    count+=1
            if count==len(banned_id):
                candidate=set(i)
                if candidate not in answer:
                    answer.append(candidate)
    return len(answer)
def check(checkid,bannedid):
    for i in range(len(checkid)):
        if bannedid[i]=="*":
            continue
        else :
            if checkid[i] == bannedid[i]:
                continue
            else:
                return False
    return True
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])