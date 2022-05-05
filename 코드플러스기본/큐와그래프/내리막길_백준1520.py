import sys

sys.setrecursionlimit(10**6)
M, N = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
answer = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
dp = [[-1 for _ in range(N)] for _ in range(M)]


def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] < graph[y][x]:
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]


print(dfs(0, 0))
