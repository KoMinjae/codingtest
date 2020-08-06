def solution(minnum,treanum):
    if minnum==treanum:
        return 0
    answer = 0
    left = 1
    count = 2
    aline=0
    a,b = min(minnum,treanum),max(minnum,treanum)
    while True:
        if a==1:
            aline=1
            break
        if left+1<=a<=left+count:
            aline=count
            break
        else:
            left=left+count
            count+=1
    count = aline
    left, right = a,a
    cnt = 1
    lfirst = sum(i for i in range(count-1,0,-1))+1
    rfirst = sum(i for i in range(count,0,-1))
    while True:
        if lfirst<=b<=rfirst:
            answer = b-a
            break
        lfirst = lfirst+count
        rfirst = rfirst+count+1
        left = left+count
        right = right+count+1
        if left<=b<=right:
            answer = cnt
            break
        elif lfirst<=b<left:
            answer=cnt+left-b
            break
        elif right<b<=rfirst:
            answer = cnt+b-right
            break
        count+=1
        cnt+=1
    return answer
print(solution(2,19))