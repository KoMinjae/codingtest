def solution(cmds):
        queue=list()
        for i in cmds:
            if "PUSH" in cmds:
                cmd, num = i.split("")
                queue.append(int(num))
            else:
                if len(queue)!=0:
                    queue.pop(0)
        return queue
    
solution(["PUSH 1","PUSH 2","PUSH 3","POP","PUSH 7","POP"])