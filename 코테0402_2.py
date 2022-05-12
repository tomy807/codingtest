def solution(n, edges, k, a, b):
    answer = -1
    graph={i:[] for i in range(n)}
    for edge in edges:
        x=edge[0]
        y=edge[1]
        graph[x].append(y)
        graph[y].append(x)
    stack=[]
    stack.append(a)
    while stack:
        out=stack.pop()
        
    return answer
solution(8, [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]], 4, 0, 3)