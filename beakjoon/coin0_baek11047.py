import sys
coinnum, total=map(int, sys.stdin.readline().split())
count_unit=[]
answer=0
for _ in range(coinnum):
    unit=int(input())
    count_unit.append(unit)
count_unit.sort(reverse=True)
for unit in count_unit:
    if(total//unit==0):
        continue
    else:
        answer+=total//unit
        total-=(total//unit)*unit
        
    if total==0:
        break
print(answer)
