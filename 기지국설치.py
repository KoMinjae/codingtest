def solution(n, stations, w):
    answer = 0
    apart = [0 for i in range(n)]
    while True:
        for i in stations:
            for i in range(i-w-1,i+w):
                if i < len(apart):
                    apart[i] = 1
        if 0 not in apart:
            break
        stations.clear()
        stations.append(len(apart)//2)
        answer+=1
    return answer

solution(11,[4,11],1)