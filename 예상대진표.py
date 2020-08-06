def solution(n,a,b):
    answer = 1
    while True:
        MA, MB = max(a,b), min(a,b)
        if MA%2==0 and MA-MB ==1:
            break
        else:
            answer+=1
            if a%2==0:
                a=a//2
            else:
                a=(a+1)//2
            if b%2==0:
                b=b//2
            else:
                b=(b+1)//2
    return answer
print(solution(8,4,7))