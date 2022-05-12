import sys
from collections import deque
blankList = []
oneToNine = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
board = []
for i in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    for j in range(9):
        if line[j] == 0:
            blankList.append((i, j))


def bfs():
    queue = deque(blankList)
    while queue:
        y, x = queue.pop()
        print(y, x)
        row = set(list((zip(*board)))[0])
        threeTmp = threeBythree(y, x)
        if len(oneToNine-set(board[y])) == 1 and 1 not in (oneToNine-set(board[y])):
            board[y][x] = (oneToNine-set(board[y])).pop()
        elif len(oneToNine-row) == 1 and 0 not in (oneToNine-row):
            board[y][x] = (oneToNine-row).pop()
        elif threeTmp != 0:
            board[y][x] = threeTmp


def threeBythree(y, x):
    startY = y//3
    startX = x//3
    threeMatrix = set()
    for i in range(startY*3, startY+3):
        for j in range(startX*3, startX+3):
            threeMatrix.add(board[i][j])
    if len(oneToNine-threeMatrix) == 1 and 0 not in (oneToNine-threeMatrix):
        return (oneToNine-threeMatrix).pop()
    else:
        return 0


bfs()
print(board)
