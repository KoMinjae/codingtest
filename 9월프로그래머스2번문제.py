def solution(n):
    answer = []
    numlist = list()
    maxnum=0
    for i in range(n):
        numlist.append([0]*(i+1))
    for i in range(n):
        numlist[i][0] = i+1
        maxnum = maxnum+len(numlist[i])
    count = n+1
    #우 좌 밑 위
    dx=[0,0,1,-1];dy=[1,-1,0,-1]
    i,j = n-1,0
    while count!=maxnum+1:
        #오른쪽으로
        if (i==n-1 and j!=n-1) or (i!=n-1 and j!=len(numlist[i])-1 and numlist[i+1][j]!=0 and numlist[i][j+1]==0):
            i=i+dx[0] ; j=j+dy[0]
            numlist[i][j]=count
    #대각위로
        elif i!=1 and (j==n-1 or numlist[i-1][j-1]==0):
            i=i+dx[3] ; j=j+dy[3]
            numlist[i][j]=count
    #대각아래로
        elif numlist[i-1][j-1]!=0 and numlist[i+1][j]==0:
            i=i+dx[2]; j=j+dy[2]
            numlist[i][j]=count
        count+=1
    ansewr = []
    for i in numlist:
        ansewr+=i
    return ansewr