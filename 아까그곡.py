def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
    answer = [[]]
    infolist = [i.split(",") for i in musicinfos]
    timelist=[[]]
    music=[[]]
    playingmusic=[]
    output=""
    for i in infolist:
        timelist.append([i[0],i[1]])
    timelist.pop(0)
    for i in infolist:
        music.append([i[2],i[3].replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')])
    music.pop(0)
    playingtime = []
    for i in timelist:
        start, end = i[0], i[1]
        if start[0] == end[0] and start[1]==end[1]:
            playingtime.append(int(end[3]+end[4])-int(start[3]+ start[4]))
        else :
            playingtime.append(abs(int(end[0]+end[1])-int(start[0]+start[1]))*60+(int(end[3]+end[4])-int(start[3]+ start[4])))
    for i in range(len(playingtime)):
        a,b = divmod(playingtime[i],len(music[i][1]))
        playingmusic.append(music[i][1]*a+music[i][1][:b])
    for i,j in enumerate(playingmusic):
        if m in j:
            answer.append([music[i][0],playingtime[i],i])
    answer.pop(0)
    if len(answer)==0:
        output="(None)"
    elif len(answer)>1:
        longtime = max(i[1] for i in answer)
        longcount=0
        for i in playingtime:
            if i == longtime:
                longcount+=1
        for i in answer:
            if longtime == i[1]:
                output=i[0]
                break
    elif len(answer)==1:
        output=answer[0][0]
    return output

print(solution("ABC", ["11:00,11:15,HELLO,ASBCDEF","12:00,12:14,HELLO1,ABCDEF", "13:00,13:16,HELLO2,ASBCDEF","13:17,13:33,HELLO3,ABCDEF","14:00,14:16,HELLO4,ABCDEF"]))