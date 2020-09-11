def solution():


def main():
    N = int(input())
    wall = set()
    apple = list()
    for i in range(N):
        wall.add((i,0))
        wall.add((0,i))
        wall.add((i,N-1))
        wall.add((N-1,i))
    movement=list()
    for i in range(int(input())):
        x,y = map(int,input().split())
        apple.append((x,y))
    for i in range(int(input())):
        x,y = map(str,input().split())
        movement.append((x,y))

main()

