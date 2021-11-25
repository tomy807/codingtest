def solution(s):
    answer = []
    count=0
    count0=0
    while True:
        if s=="1":
            break
        count0+=s.count("0")
        count+=1
        s=s.replace("0","")
        s=bin(len(s))[2:]
    return [count,count0]

print(solution("110010101001"))
