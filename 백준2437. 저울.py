def solution(N, grams):
    grams.sort()
    answer = 1
    for i in range(N):
        if answer < grams[i]:
            break
        else:
            answer+=grams[i]
    return answer

def main():
    N = int(input())
    grams = list(map(int,input().split()))
    print(solution(N, grams))

main()