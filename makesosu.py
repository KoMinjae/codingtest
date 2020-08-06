import math,itertools
def solution(num):
    answer = 0
    numlist = list(num)
    numlist.sort()
    maxnum = sum(numlist[-3:])
    Eratos = [1 for i in range(maxnum+1)]
    Eratos[0], Eratos[1] = 0,0
    for i in range(2, int(maxnum**0.5)+1):
        j=i
        if(Eratos[i]==1):
            j+=i
            while(j <= maxnum):
                Eratos[j] = 0
                j+=i
    sumlist = list((itertools.combinations(num,3)))
    for i in sumlist:
        if Eratos[sum(i)] == 1:
            answer+=1
    return answer
solution([1,2,3,4])