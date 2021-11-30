import sys
M,N,K=map(int,sys.stdin.readline().split(' '))
# Map=[[0]*(N)]*(M) 절대 사용X
graph = [list([0] * N) for _ in range(M)]
# for _ in range(K):
#     x0,y0,x1,y1=map(int,sys.stdin.readline().split(' '))
#     for j in range(y0,y1):
#         for i in range(x0,x1):
#             Map[j][i]=1
print(Map)
print(graph)
#(0,2) (4,4)
# 00 01 02 03 04 05 06
# 10 11 12 13 14 15 16
# 20 21 22 23 24 25 26
# 30 31 32 33 34 35 36
# 40 41 42 43 44 45 46
# 50 51 52 53 54 55 56