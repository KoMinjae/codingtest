def solution(num):
    numarr = [str(i+1) for i in range(num-1)]
    strarr =list()
    for i in numarr:
        if "3" in i or "6" in i or "9" in i:
            strarr.append(i)
    print(strarr.count("3")+strarr.count("6")+strarr.count("9"))
solution(40)