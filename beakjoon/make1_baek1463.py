import sys
def solve(n):
    for i in range(n):
        li=[]
        for num in N[i]:
            if num==1:
                return(i)
            if num%3==0:
                li.append(num/3)
            if num%2==0:
                li.append(num/2)
            li.append(num-1)
        N.append(li)
n=int(sys.stdin.readline())
N=[]
N.append([n])
print(solve(n))