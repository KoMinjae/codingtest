import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = [0 for _ in range(len(arr))]
stack = []

for i in range(len(arr)-1, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = i+1
    stack.append(i)
print(*answer)