def solution(number, k):
    numlist=list(number)
    collect=[]
    for i, num in enumerate(number):
        while k > 0 and number and len(collect) > 0 and collect[-1] < num:
            collect.pop()
            k-=1
        if k == 0:
            collect += list(number[i:])
            break
        collect.append(num)
    collect = collect[:-k] if k > 0 else collect
    answer = ''.join(collect)
    return answer

solution("1231234",3)