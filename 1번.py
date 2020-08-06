from collections import Counter
def solution(p):
    answer = 0
    while True:
        a=Counter(str(year))
        if len(a) == len(str(p)):
            return p
        else:
            p+=1
  

solution(1988)