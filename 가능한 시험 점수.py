def solution(score):
    scoresum=set()
    scoresum.add(0)
    for i in score:
        scores=list()
        for j in scoresum:
            if i + j not in scoresum:
                scores.append(i+j)
        for i in scores:
            scoresum.add(i)
    return len(scoresum)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count=int(input())
    if count ==0:
        print("#"+str(test_case),0)
    else:
        N=list(map(int,input().split()))
        print("#"+str(test_case),solution(N))
