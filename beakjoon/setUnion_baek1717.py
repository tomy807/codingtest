import sys

def union(a,b):
    x=find(a)
    y=find(b)
    if x==y:
        return
    parent[y]=x

def find(x):
    if parent[x]==x:
        return x
    parent[x]= find(parent[x])
    return parent[x]

def check(a,b):
    x=find(a)
    y=find(b)
    if x==y:
        return "YES"
    return "NO"

n,m=map(int,sys.stdin.readline().split(' '))
parent=[i for i in range(n+1)]
for _ in range(m):
    o,a,b=map(int,sys.stdin.readline().split(' '))
    if o==0:
        union(a,b)
    elif o==1:
        print(check(a,b))