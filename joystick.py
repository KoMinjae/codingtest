def solution(name):
    answer = 0
    name = list(name)
    alist = ["A"] * len(name)
    idx = 0 
    if name == alist:
        return 0
    else : 
        while True :
            ridx = 1
            lidx = 1
            if name[idx] != "A":
                num = ord(name[idx])
                answer += min(num-65, 91-num)
                name[idx]="A"
            if name == alist :
                break
            else:
                for i in range(1,len(name)):
                    if name[idx+i] == "A":
                        ridx += 1
                    else :
                        break
                    if name[idx-i] == "A":
                        lidx +=1
                    else:
                        break
                if ridx>lidx:
                    answer +=lidx
                    idx -= lidx
                else :
                    answer+=ridx
                    idx+=ridx   
    return answer
solution("JAN")