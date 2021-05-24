from collections import deque
def bfs(x, y,array) :
    n=len(array)
    m=len(array[0])
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            if(nx<0 or nx>=n or ny<0 or ny>=m) : continue
            if array[nx][ny] == 0 : continue
            if(array[nx][ny]==1) :
                queue.append((nx, ny))
                array[nx][ny]=array[x][y]+1
    return array[n-1][m-1]
def solution(maps):
    answer=0
    answer=bfs(0, 0, maps)
    if answer==1:
        return -1
    else:
        return answer
