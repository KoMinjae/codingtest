numset = {str(x) for x in range(10)}

N = int(input())
M = int(input())
if(M == 0):
    pass
else:
    breakset = set(input().split())
    nums=numset.difference(breakset)

answer = abs(N - 100)
for i in range(1000001):
    check = True
    for div_num in str(i):
        if(div_num not in nums):
            check = False
    if(check):
        answer = min(answer, abs(N - i) + len(str(i)))

print(answer)