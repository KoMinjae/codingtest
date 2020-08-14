###배열을 이용한 트리 구현###
def inorder(node):
    if node:
        inorder(arr[node][2])
        answer.append(arr[node][1])
        inorder(arr[node][3])


for tc in range(10):
    n = int(input())
    arr = [[0]*4 for i in range(n+1)]
    for i in range(n):
        data = list(input().split())
        arr[int(data[0])][0] = int(data[0])
        arr[int(data[0])][1] = data[1]
        if len(data) >= 3:
            arr[int(data[0])][2] = int(data[2])
        if len(data) == 4:
            arr[int(data[0])][3] = int(data[3])

    answer = []
    inorder(1)
    print('#{}'.format(tc+1), end=' ')
    for i in answer:
        print(i,end='')
    print()