def solution(n):
    K=0
    while  n> 0:
        d,m = divmod(n,2)
        n=d
        if m!=0:
            K+=1
    return K

solution(6)