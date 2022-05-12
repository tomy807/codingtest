import sys
from itertools import combinations
N=int(input())
board=[]
answer=100000
setN={i for i in range(N)}
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split(' '))))
visited=[0 for _ in range(N)]
teamA=[]
for i in range(2,int(N/2)):
    teamA.extend(combinations(list(i for i in range(N)), i))
for team in teamA:
    sumA=0
    sumB=0
    for i in range(len(team)):
        for j in range(i+1,len(team)):
            sumA+=board[team[i]][team[j]]
            sumA+=board[team[j]][team[i]]
    teamb=list(setN-set(team))
    for i in range(len(teamb)):
        for j in range(i+1,len(teamb)):
            sumB+=board[teamb[i]][teamb[j]]
            sumB+=board[teamb[j]][teamb[i]]
    answer=min(answer,abs(sumA-sumB))
    if answer==0:
        break
print(answer)