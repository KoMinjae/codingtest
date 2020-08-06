import re
 
def solution(s):
    regx=r'[{][\d,]+[}]'
    answer =[]
    tuplist = list(re.findall(regx,s))
    tuplist.sort(key= lambda x : len(x))
    for i in tuplist:
        for j in i:
            if j is not '{' and j is not '}' and j is not',' :
                if int(j) not in answer:
                    answer.append(int(j))     
    return answer
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))