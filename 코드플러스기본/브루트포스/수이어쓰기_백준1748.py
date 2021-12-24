N=int(input())
lenghtN=len(str(N))
answer=0
for i in range(1,lenghtN):
    answer+=i*(int('9'+'0'*(i-1)))
answer+=(N-10**(lenghtN-1)+1)*lenghtN
print(answer)