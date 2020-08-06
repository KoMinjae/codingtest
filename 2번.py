def change(number, base):
    note = '01234'
    q, r= divmod(number, base)
    n = note[r]
    return change(q,base) + n if q else n
def solution(n):
    answer=0
    numlist =list()
    i=1
    count=1
    while len(numlist)!=n:
        num = change(i,3)
        if '2' not in num:
            numlist.append(change(i,3))
        i+=1
    for i in range(len(numlist[-1])-1,-1,-1):
        answer+=int((numlist[-1][i]))*count
        count=count*3
    return answer
solution(11)