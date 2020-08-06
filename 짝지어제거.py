def solution(s):
    answerlist=list(s)
    checklist=[]
    for i in s:
        checklist.append(i)
        if len(checklist)>1:
            if checklist[-1] == checklist[-2]:
                checklist.pop()
                checklist.pop()
        if checklist == answerlist:
            return 0
    if len(checklist)== 0:
        return 1    
    else:
        return 0
        
        
print(solution("abccaeeaba"))