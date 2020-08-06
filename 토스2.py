import copy
def solution(lotto):
    checklist=copy.deepcopy(lotto)
    checklist.sort()
    if len(checklist)!=6:
    	return False
    if checklist!=lotto:
        return False
    checklist
    for i in checklist:
        if checklist.count(i) != 1:
            return False
        if i > 46:
            return False
    return True
    

user_input = list(map(int,list(input().split())))

solution(user_input)