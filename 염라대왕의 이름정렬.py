T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    namelist=list()
    for i in range(N):
        name=input()
        namelist.append((name,len(name)))
    namelist=list(set(namelist))
    namelist.sort(key= lambda x:(x[1],x[0]))
    print('#{}'.format(test_case))
    for i in namelist:
        print(i[0])
