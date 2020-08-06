def changedigit(number, base):
    alpha = '0123456789ABCDEF'
    i, j =divmod(number,base)
    if i == 0:
        return alpha[j]
    else :
        return changedigit(i, base) + alpha[j]
def solution(n, t, m, p):
    numlist=''
    answer = []
    startnum = 0
    tubeturn = p
    idx=0
    while len(numlist)<t*m:
        changenum = changedigit(startnum, n)
        numlist+=changenum                  
        startnum+=1
    for i in range(t):
        answer.append(numlist[tubeturn-1])
        tubeturn+=m
    return ''.join(answer)

solution(16,16,2,1)