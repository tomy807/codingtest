import collections
def solution(board, moves):
    answer = 0
    dqlist=[]
    collect=[]
    stack=[]
    new_board=list((map(list,zip(*board)))) #리스트 뒤집기!!
    for i in range(len(new_board)):     #각 줄마다 deque 만들어서 list에 넣기
        deq=collections.deque(new_board[i])
        dqlist.append(deq)
    for i in moves:     #moves에 따라 deque에서 pop
        while True:
            if dqlist[i-1]:
                a=dqlist[i-1].popleft()
                if a!=0:
                    collect.append(a)      #0이 나오면 숫자가 나올때까지 pop, 나온 숫자를 collect에 넣기
                    break
            else:
                break
    collect_dq=collections.deque(collect)
    a=collect_dq.popleft()
    stack.append(a)
    while collect_dq:
        b=collect_dq.popleft()
        if stack:
            if stack[-1]==b:
                stack.pop()
                answer=answer+2
            else:
                stack.append(b)
        else:
            stack.append(b)
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
