import sys
def solution(lines,N):
    lines.sort(key = lambda x:(x[0],-x[1]))
    answer = lines[0][1]-lines[0][0]
    tempstart=lines[0][0]; tempend=lines[0][1]
    for i in range(1,N):
        start = lines[i][0]
        end = lines[i][1]
        if start >= tempend:
            answer += end-start
            tempstart = start; tempend = end
        elif tempstart <= end <= tempend:
            continue
        elif start <= tempend and end >= tempend:
            answer+= end - tempend
            tempend=end
    return answer
def main():
    N = int(input())
    lines = list()
    for i in range(N):
        line = list(map(int,(sys.stdin.readline().split())))
        lines.append(line)
    print(solution(lines,N))

main()