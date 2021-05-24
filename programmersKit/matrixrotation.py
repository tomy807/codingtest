from collections import deque
def solution(rows, columns, queries):
    answer = []
    matrix= [[0 for j in range(columns+1)] for i in range(rows+1)]
    for j in range(1,columns+1):
        for i in range(1,rows+1):
            matrix[i][j]=(i-1)*columns+j
    deq=deque()
    for querie in queries:
        for j in range(querie[1],querie[3]):
            deq.append(matrix[querie[0]][j])
        for i in range(querie[0],querie[2]):
            deq.append(matrix[i][querie[3]])
        for j in range(querie[3],querie[1],-1):
            deq.append(matrix[querie[2]][j])
        for i in range(querie[2],querie[0],-1):
            deq.append(matrix[i][querie[1]])
        deq.rotate(1)
        answer.append(min(deq))
        for j in range(querie[1],querie[3]):
            matrix[querie[0]][j]=deq.popleft()
        for i in range(querie[0],querie[2]):
            matrix[i][querie[3]]=deq.popleft()
        for j in range(querie[3],querie[1],-1):
            matrix[querie[2]][j]=deq.popleft()
        for i in range(querie[2],querie[0],-1):
            matrix[i][querie[1]]=deq.popleft()
    return answer
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))