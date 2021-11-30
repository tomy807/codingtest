def solution(n, k, cmd):
    answer = ''
    graph=[i for i in range(n)]
    point=k
    deletelist=[]
    for commands in cmd:
        command=commands[0]
        if command=="U":
            count=commands[2]
            k-=count
        elif command=="D":
            count=commands[2]
            k+=count
        elif command=="C":
            if count==len(graph):
                count-=1
            deletelist.append(graph[count])
            del graph[count]
        else:
            pass
    return answer


#U:up D:down C:지우고 아래행 선택 Z: 마지막에 지운거 복구 point 그래도