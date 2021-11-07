def solution(rows, columns):
    graph = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    recent=1
    graph[1][1]=recent
    r=1
    c=1
    while(True):
        if is0(graph,rows,columns):
            if r==1 and c==1 and recent>1 and recent%2==1:
                newgraph = [[0 for _ in range(columns)] for _ in range(rows)]
                for i in range(1,rows+1):
                    for j in range(1,columns+1):
                        newgraph[i-1][j-1]=graph[i][j]
                return newgraph
            if recent%2==0:
                if r==rows:
                    r=1
                else:
                    r+=1
            elif recent%2==1:
                if c==columns:
                    c=1
                else:
                    c+=1
                    
            recent+=1
            graph[r][c]=recent
        else:
            newgraph = [[0 for _ in range(columns)] for _ in range(rows)]
            for i in range(1,rows+1):
                for j in range(1,columns+1):
                    newgraph[i-1][j-1]=graph[i][j]
            return newgraph
        
    return newgraph

def is0(graph,rows,columns):
        for i in range(1,rows+1):
            for j in range(1,columns+1):
                if graph[i][j]==0:
                    return True
        return False
print(solution(3, 3))