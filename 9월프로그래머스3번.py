import copy
def solution(numlist):
    answer = list()
    for i in range(3,len(numlist)):
        num = numlist[i]
        a = copy.deepcopy(numlist)
        while True:
            if a.index(num)==0 or a.index(num)==1:
                if len(a)==3:
                    break
                elif len(a)==2:
                    answer.append(num)
                    break
                for j in range(len(a)-1,a.index(num),-1):
                    if a[j]>a[j-1]:
                        a.pop(j)
                    elif j==a.index(num)+1:
                        if a[a.index(num)]>a[j-1]:
                            break
                    else:
                        a.pop(j-1)
                    
                    
            else:
                for j in range(a.index(num)-1,-1,-1):
                    if a[j]>a[j-1]:
                        a.pop(j)
                    elif j==1:
                        if a[j]>a[j-1]:
                            break
                    else:
                        a.pop(j-1)
                    

    return answer

solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])