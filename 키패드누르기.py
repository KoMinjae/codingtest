distdir2={1:1,4:2,7:3,3:1,6:2,9:3,5:1,8:2,0:3,10:4,20:4,2:0}
distdir5={1:2,4:1,7:2,3:2,6:1,9:2,2:1,8:1,0:2,10:3,20:3,5:0}
distdir8={1:3,4:2,7:1,3:3,6:2,9:1,2:2,5:1,0:1,10:2,20:2,8:0}
distdir0={1:4,4:3,7:2,3:4,6:3,9:2,2:3,5:2,8:1,10:1,20:1,0:0}
def getdist(num,lnow,rnow):
    if num == 2:
        ldist, rdist = distdir2[lnow],distdir2[rnow]
    elif num == 5:
        ldist, rdist = distdir5[lnow],distdir5[rnow]
    elif num == 8:
        ldist, rdist = distdir8[lnow],distdir8[rnow]
    elif num == 0:
        ldist, rdist = distdir0[lnow],distdir0[rnow]
    return ldist,rdist
def solution(numbers, hand):
    answer = list()
    left = [1,4,7]
    right = [3,6,9]
    lnow = 10
    rnow = 20
    nownum = 0
    for i in numbers:
        if i in left:
            answer.append("L")
            lnow = i
        elif i in right:
            answer.append("R")
            rnow = i
        else:
            ldist, rdist = getdist(i,lnow,rnow)
            if ldist > rdist:
                answer.append("R")
                rnow = i
            elif ldist<rdist:
                answer.append("L")
                lnow = i
            elif ldist == rdist :
                if hand == "right":
                    answer.append("R")
                    rnow = i
                else :
                    answer.append("L")
                    lnow = i
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))