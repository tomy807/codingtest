import sys
N,M=map(int, input().split(' '))
r,c,d =map(int, input().split(' '))
matrix= [list(map(int, input().split())) for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def clean(r,c,d):
    cnt=0
    while(True):
        y=r
        x=c
        nd=turnLeft(d)
        for i in range(4):
            if 0<=y<N and 0<=x<M and matrix[y][x]==0 :
                matrix[y][x]=2
                cnt+=1
            