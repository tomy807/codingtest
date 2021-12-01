change=1000-int(input())
answer=0
units=[500,100,50,10,5,1]
for unit in units:
    tmp,change=divmod(change, unit)
    answer+=tmp
print(answer)