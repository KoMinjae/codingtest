from math import ceil
def solution(n, words):
    answer = []
    checklist = []
    checklist.append(words[0])
    for i, j in enumerate(words):
        if i!=0:
            if not j in checklist:
                checklist.append(j)
            else:
                answer.append((i+1)%n if ((i+1)%n)!=0 else n)
                answer.append(ceil((i+1)/n))
                break
            if checklist[i-1][-1] != j[0]:
                answer.append((i+1)%n if ((i+1)%n)!=0 else n)
                answer.append(ceil((i+1)/n))
                break
    if len(answer)==0:
        answer.append(0)
        answer.append(0)
    return answer

print(solution(2,["land", "dream", "mom", "mom", "ror"]))