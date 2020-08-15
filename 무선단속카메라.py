T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    K= int(input())
    cameralist = sorted(list(set(map(int,input().split()))))
    if K >= len(cameralist):
        print('#{} {}'.format(test_case, 0))
        continue
    dist = list()
    for i in range(len(cameralist)-1):
        dist.append(cameralist[i+1]-cameralist[i])
    dist.sort()
    while K!=1:
        dist.pop()
        K-=1
    print('#{} {}'.format(test_case, sum(dist)))
