import pprint
from collections import deque
M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []
totalCount = 0
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1


def bfs(x, y):
    count = 0
    queue = deque([(x, y)])
    while queue:
        out = queue.popleft()
        count += 1
        for i in range(4):
            ny = out[1]+dy[i]
            nx = out[0]+dx[i]
            if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 0:
                graph[ny][nx] = -1
                queue.append((nx, ny))
    return count


for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = -1
            answer.append(bfs(j, i))
            totalCount += 1
answer.sort()
print(totalCount)
print(*answer)
