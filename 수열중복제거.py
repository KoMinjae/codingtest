def solution(sequence):
    setlen=len(set(sequence))
    count=0
    while len(sequence)!=setlen:
        if sequence.count(sequence[count])!=1:
            sequence.remove(sequence[count])
        else:
            count+=1
    return sequence
print(solution([1,5,5,1,6,1]))