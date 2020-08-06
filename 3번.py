class Node(object):
       def __init__(self, data):
           self.data = data
           self.children = []

def solution(total_sp, skills):
    answer = []
    highskill=list()
    realhighskill=0
    for i in skills:
        if i[0] not in highskill:
            highskill.append(i[0])
    j=0
    while j!=len(highskill):
        for i in range(len(skills)):
            if highskill[j] == skills[i][1]:
                highskill[j]=0
        j+=1
    for i in highskill:
        if i != 0:
            realhighskill = i
    Node(realhighskill,0)
    for i in skills:
        if 
    return answer

solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]])