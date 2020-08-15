from itertools import permutations

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    answer=0
    numlist = list(map(int,input().split()))
    permus = list(permutations(numlist))
    leftsum=0
    rightsum=0
    for i in permus:
        leftsum=sum(i)
        for j in range(len(i)):
            if leftsum-i[j] <rightsum+i[j]:
                leftsum-=i[j]
                rightsum+=i[j]
                answer+=1
    print('#{} {}'.format(test_case, answer))
        