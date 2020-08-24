def solution(MAPS):
    maxs = 0
    result=0
    for i in range(100):
        if maxs<result:
            maxs=result
        result=0
        for j in range(100):
            result+=MAPS[i][j]
    for i in range(100):
        if maxs<result:
            maxs=result
        result=0
        for j in range(100):
            result+=MAPS[j][i]

    for i in range(100):
        if maxs<result:
            maxs=result
        result=0
        for j in range(100):
            if i == 100-j:
                result += MAPS[i][j]
    return maxs

def main():
    for test_case in range(1,11):
        T=int(input())
        MAPS=list()
        for i in range(100):
            submap = list(map(int, input().split()))
            MAPS.append(submap)
        print("#{} {}".format(test_case, solution(MAPS)))

main()