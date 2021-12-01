T=int(input())
button=[300,60,10]
if T%10!=0:
    print(-1)
else:
    for time in button:
        a,T=divmod(T, time)
        print(a)