import sys
from itertools import combinations
people=[]
for _ in range(9):
    people.append(int(sys.stdin.readline()))
comList=combinations(people, 7)
for combi in comList:
    if sum(combi)==100:
        for i in sorted(list(combi)):
            print(i)
        break