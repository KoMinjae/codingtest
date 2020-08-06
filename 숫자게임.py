def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for a in A[::-1]:
        if B[-1]>a:
            answer+=1
            B.pop(-1)
    return answer

solution([5,1,3,7],[2,2,6,8])