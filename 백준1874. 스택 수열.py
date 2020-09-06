N = int(input())
stack=list()
maxhigh = 0
answer = list()
maxnum=0
for i in range(N):
    nownum = int(input())
    while nownum > maxnum:
        stack.append(maxnum+1)
        answer.append("+")
        maxnum+=1
    if stack[-1] == nownum:
        stack.pop()
        answer.append("-")

if not stack:
    for i in answer:
        print(i)
else:
    print("NO")


