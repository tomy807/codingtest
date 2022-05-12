from sys import stdin


def visitable(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]


def dfs(cnt, start, cur, color):
    for x, y in dirs:
        next_x, next_y = cur[X] + x, cur[Y] + y

        if cnt >= 4 and start == [next_x, next_y]:
            print('Yes')
            exit()

        if visitable(next_x, next_y) and graph[next_x][next_y] == color:
            visited[next_x][next_y] = True
            dfs(cnt + 1, start, [next_x, next_y], color)
            visited[next_x][next_y] = False


if __name__ == "__main__":
    answer = False
    X, Y = 0, 1
    n, m = map(int, stdin.readline().split())
    graph = [list(stdin.readline().strip()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                visited[x][y] = True
                dfs(1, [x, y], [x, y], graph[x][y])

    print('No')
