N,K=map(int,input().split())
answer=1
for n in range(N,N-K,-1):
    answer*=n
for k in range(1,K+1):
    answer=answer/k
print(int(answer%1000000007))