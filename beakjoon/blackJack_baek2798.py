import sys
from itertools import combinations
N,M=map(int,sys.stdin.readline().split(' '))
cards=list(map(int,sys.stdin.readline().split(' ')))
tmp=0
for card3 in combinations(cards,3):
    sumCards=sum(card3)
    if tmp<=sumCards<=M:
        tmp=sumCards
print(tmp)
