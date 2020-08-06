def solution(nums):
    answer = 0
    q=list()
    nums.sort()
    maxpoket=len(nums)/2
    count=0
    howmany=set(nums)
    q.append(nums.pop(0))
    while count<maxpoket:
        if q[-1]!=nums[0]:
            q.append(nums.pop(0))
            count+=1
        elif q[-1]==nums[0]:
            nums.pop(0)
        if len(nums)==0:
            break
    if len(q)>maxpoket:
        return int(maxpoket)
    return len(q)

solution([3,1,2,3])