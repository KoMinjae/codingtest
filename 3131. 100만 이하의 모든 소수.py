eratos=[0]*1000000
for i in range(2,1000):
    x=0
    if eratos[i] == 0:
        x=i
        x=x+i
        while x<1000000:
            eratos[x]=1
            x=x+i
sosu=list()
for i in range(2,1000000):
    if eratos[i] == 0:
        sosu.append(str(i))
print(' '.join(sosu))