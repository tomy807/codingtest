from collections import deque

def solution(places):
    answer = []
    for place in places:
        locationsP=findP(place)
        result=resultFind(locationsP,place)            
        answer.append(result)
    return answer

def resultFind(locationsP,place):
    for locationP in locationsP:
            board=bfs(locationP,place)
            print(board)
            for otherLocationP in locationsP:
                if locationP !=otherLocationP:
                    if -1<board[otherLocationP[0]][otherLocationP[1]]<=2:
                        return 0
    return 1
def bfs(locationP,place):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue=deque()
    board=[[-1 for _ in range(5)] for _ in range(5)]
    queue.append([locationP[0],locationP[1]])
    board[locationP[0]][locationP[1]]=0
    while(queue):
        y,x=queue.popleft()
        for i in range(4):
            newY=y+dy[i]
            newX=x+dx[i]
            if isin(newY,newX) and place[newY][newX]!='X' and board[newY][newX]==-1:
                board[newY][newX]=board[y][x]+1
                queue.append([newY,newX])
    return board
def isin(newY,newX):
    if -1<newY<5 and -1<newX<5:
        return True
    return False

def findP(place):
    locationsP=[]
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P':
                locationsP.append([i,j])
    return locationsP        

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))