def solution(N,lines):
    solline=[0]*N
    solline[0] = lines[0]
    solline[1] = solline[0]+lines[1]
    solline[2] = max(lines[1]+lines[2], lines[0]+lines[2])
    for i in range(3,N):
        solline[i] = max(solline[i-3]+lines[i-1]+lines[i], solline[i-2]+lines[i])
    return solline[-1]
def main():
    N = int(input())
    lines=list()
    for i in range(N):
        line = int(input())
        lines.append(line)
    print(solution(N,lines))
main()