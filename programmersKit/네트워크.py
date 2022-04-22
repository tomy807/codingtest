from collections import deque
global visited
visited=set()
def solution(n, computers):
    answer=0
    global visited
    for i in range(n):
        if i in visited:
            continue
        else:
            bfs(i, computers, n)
            answer+=1
    return answer

def bfs(i,computers,n):
    global visited
    queue=deque([])
    queue.append(i)
    while queue:
        out=queue.popleft()
        visited.add(out)
        for j in range(n):
            if out!=j and j not in visited and computers[out][j]==1:
                queue.append(j)

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))