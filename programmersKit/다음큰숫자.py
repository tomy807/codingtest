def solution(n):
    bin1Count=bin(n).count('1')
    for i in range(n+1,1000000):
        count=bin(i).count('1')
        if(bin1Count==count):
            return i
print(solution(15))