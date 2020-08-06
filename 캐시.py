def solution(cacheSize, cities):
    answer = 0
    city = list(cities)
    citystack = []
    if cacheSize==0:
        return 5*len(cities)
    for i in city:
        j=i.upper()
        if not j in citystack:
            answer+=5
            if len(citystack) == cacheSize:
                citystack.pop(0)
                citystack.append(j)
            else:
                citystack.append(j)
        elif j in citystack:
            answer+=1
            citystack.pop(citystack.index(j))
            citystack.append(j)
    return answer

solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])