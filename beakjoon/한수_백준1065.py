import sys

N=int(sys.stdin.readline())
hundred=[]
if N<100:
    print(N)
elif len(str(N))==3:
    for i in range(1,10):
        for dx in range(-10,10):
            answer=str(i)
            if -1<i+dx<10 and -1<i+2*dx<10:
                answer+=str(i+dx)+str(i+dx*2)
                hundred.append(int(answer))
    count=0
    print(hundred)
    for i in hundred:
        if i <=N:
            count+=1
    print(99+count)
else:
    print(144)