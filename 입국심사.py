def solution(n, times):
    answer = 0
    times.sort()
    left, right = 0, times[-1] * n
    while left <= right:
        mid = (left+right) // 2
        people = 0
        for i in times:
            people += mid//i
        if people >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer
solution(6,[7,10])