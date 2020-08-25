def solution(MAPS):
    count=0
    for j in range(100):
        stack=list()
        check = False
        for i in range(100):
            if MAPS[i][j] == 1:
                stack.append(1)
            if MAPS[i][j] == 2 and stack:
                stack.clear()
                count += 1
    return count

def main():
    
    for test_case in range(1,11):
        T = int(input())
        MAPS=list()
        for i in range(100):
            lines = list(map(int,input().split()))
            MAPS.append(lines)
        print("#{} {}".format(test_case, solution(MAPS)))

main()