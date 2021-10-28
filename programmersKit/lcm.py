def solution(arr):
    a=1
    for i in arr:
        a=lcm(a,i)
    return int(a)

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

print(solution([2,6,8,14]))