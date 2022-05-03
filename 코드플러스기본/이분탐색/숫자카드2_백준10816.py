import sys
N=int(input())
cards=list(map(int,sys.stdin.readline().split()))
M=int(input())
targets=list(map(int,sys.stdin.readline().split()))
targetDict={i:0 for i in targets}
for card in cards:
    if card in targetDict.keys():
        targetDict[card]+=1
print(' '.join(str(targetDict[m]) if m in targetDict else '0' for m in targets))