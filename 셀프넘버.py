def solution(a):
    selfnum=[0 for i in range(a)]
    selfnum[1] = 0
    for i in range(1,a):
        checknum=i
        for j in str(i):
            checknum+=int(j)
        if checknum <=a:
            selfnum[checknum-1]+=1
    return selfnum[a-1]
solution(101)