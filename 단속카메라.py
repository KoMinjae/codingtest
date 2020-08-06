def solution(routes):
    answer = 1
    routes.sort(key = lambda x : abs(x[0]-x[1]))
    routes.sort(key=lambda x: -x[0])
    camera=list()
    camera.append(routes[0][0])
    X=True
    for i in routes:
        check=len(camera)
        idx=0
        while X==True:
            if i[0]<= camera[idx] <=i[1]:
                break
            else :
                if check-1 == idx:
                    camera.append(i[0])
                    answer+=1
                    break
                idx+=1
    return answer

solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])