formulas=input().split('-')
answer=0
answer+=sum(map(int,formulas[0].split('+')))
for i in formulas[1:]:
    answer-=sum(map(int,i.split('+')))
print(answer)