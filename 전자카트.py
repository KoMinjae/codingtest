def solution(N,MAPS):
    answer=list()
    stack=list()
    stack.append((0,["0"],0))
    while stack:
        v, path, point = stack.pop()
        if len(path)==N:
            answer.append((point+MAPS[v][0]))
        else:
            for i in range(len(MAPS[v])):
                if MAPS[v][i]!=0 and str(i) not in path:
                    stack.append((i,path+list(str(i)),point+MAPS[v][i]))
                    
    return min(answer)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N=int(input())
    MAPS=[list(map(int,input().split())) for _ in range(N)]
    print("#"+str(test_case), solution(N,MAPS))
###
""" 3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
 """
#1 89
#2 96
#3 139
###