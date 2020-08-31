from collections import Counter
for test_case in range(1, int(input())+1):
    answer = 0
    i = int(input())
    numlist = list(map(int, input().split()))
    answer = Counter(numlist).most_common(1)
    print("#{} {}".format(test_case,answer[0][0]))