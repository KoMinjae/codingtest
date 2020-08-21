def solution(croaks):
    stack=list()
    croaks=list(croaks)
    croaklist=[0]*5
    count = 0
    for i in croaks:
        if i == "c":
            stack.append(i)
            croaklist[0]=croaklist[0]+1
            count = max(count, croaklist[0])
        elif i == "r":
            if "c" in stack:
                if stack.count("c") > stack.count("r"):
                    stack.append(i)
                    croaklist[1]=croaklist[1]+1
                else:
                    return -1
            else:
                return -1
        elif i == "o":
            if "c" in stack and "r" in stack:
                if stack.count("r") > stack.count("o"):
                    stack.append(i)
                    croaklist[2]=croaklist[2]+1
                else:
                    return -1
            else:
                return -1
        elif i == "a":
            if "c" in stack and "r" in stack and "o" in stack:
                if stack.count("o") > stack.count("a"):
                    stack.append(i)
                    croaklist[3]=croaklist[3]+1
                else:
                    return -1
            else:
                return -1
        elif i == "k":
            if "c" in stack and "r" in stack and "o" in stack and "a" in stack:
                if stack.count("a") > stack.count("k"):
                    stack.append(i)
                    croaklist[4]=croaklist[4]+1
                    stack.pop(stack.index("c"))
                    stack.pop(stack.index("r"))
                    stack.pop(stack.index("o"))
                    stack.pop(stack.index("a"))
                    stack.pop(stack.index("k"))
                    for j in range(4):
                        croaklist[j]=croaklist[j]-1
                else:
                    return -1
            else:
                return -1
    if stack:
        return -1
    return count

def main():
    T = int(input())

    for test_case in range(1,T+1):
        croak = input()
        print('#{} {}'.format(test_case, solution(croak)))

main()
