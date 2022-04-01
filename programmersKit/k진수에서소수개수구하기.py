import math
def solution(n, k):
    answer=0
    div3=''
    while n>0:
        n,mod=divmod(n, k)
        div3+=str(mod)
    div3=div3[::-1]
    splitN=div3.split('0')
    for i in splitN:
        if(i==""):
            continue
        if isPrime(int(i)):
            answer+=1
    return answer

def isPrime(n):
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False 
    return True

print(solution(110011,10))