def solution(lists):
    answer = list()
    answer.append(lists[0])
    lists.pop(0)
    for i in lists:
        print(' '.join(answer))
        if len(answer)==5:
            if i not in answer:
                answer.pop(-1)
                answer.insert(0,i)
                continue
        if i in answer:
            if answer.index(i)==0:
                continue
            else:
                answer.pop(answer.index(i))
                answer.insert(0,i)
        else:
            answer.insert(0,i)
    return ' '.join(answer)
user_input = list(input().split(" "))
print(solution(user_input))