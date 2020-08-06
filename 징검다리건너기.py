def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    while left<=right:
        mid = (left+right)//2
        zerocount=0
        for i in stones:
            if i<mid:
                zerocount+=1
            else:
                zerocount=0
            if zerocount>=k:
                right=mid-1
                break
        if zerocount<k:
            left=mid+1
            answer=mid
    return answer

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	,3)