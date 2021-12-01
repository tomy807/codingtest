S=int(input())
n=1
while(True):
    tmp=S-(n*(n+1))//2
    if tmp<=n:
        print(n)
        break
    n+=1

