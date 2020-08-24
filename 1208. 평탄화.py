def solution(boxs,num):
    for i in range(num):
        boxs[boxs.index(max(boxs))]-=1
        boxs[boxs.index(min(boxs))]+=1
    return max(boxs) - min(boxs)

def main():
    for test_case in range(1, 11):
        num=int(input())
        boxs = list(map(int,input().split()))
        print('#{} {}'.format(test_case, solution(boxs,num)))

main()