def solution(lines):
    dp=[1]*len(lines)
    for i in range(len(lines)):
        for j in range(i):
           if lines[i] > lines[j]: 
               dp[i] = max(dp[i], dp[j]+1)
    return len(lines)-max(dp)
def main():
    lines = list()
    for i in range(int(input())):
        lines.append(int(input()))

    print(solution(lines))

main()