import itertools
graph=dict()
def solution(word):
    answer = 0
    aeiou=["A","E","I","O","U"]
    lists1 = list(itertools.product(aeiou,repeat=1))
    lists2 = list(itertools.product(aeiou,repeat=2))
    lists3 = list(itertools.product(aeiou,repeat=3))
    lists4 = list(itertools.product(aeiou,repeat=4))
    lists5 = list(itertools.product(aeiou,repeat=5))
    lists6 = lists1+lists2+lists3+lists4+lists5
    for i in range(len(lists6)):
        lists6[i]="".join(lists6[i])

    lists6.sort(key = lambda x:x)
    answer = lists6.index(word)
    return answer+1

solution("I")