def solution( x1, m1, x2, m2):
        
        left, right = 1, 10000
        while left<=right:
            mid = (left+right)/2
            a= float((m1*m2)/((x1-mid)*(x1-mid)))
            b=float((m1*m2)/((x2-mid)*(x2-mid)))
            if a == b:
                return mid
            elif a > b:
                left=mid
            elif a < b:
                right=mid
        return 0

solution(1,1,2,1000)