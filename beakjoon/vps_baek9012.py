def solution(line):
    stack=[]
    for vps in line:
        if(vps=='('):
            stack.append(vps)
        else:
            if(len(stack)==0):
                return 'NO'
            else:
                stack.pop()
    if(len(stack)>0):
        return 'NO'
    else:
        return 'YES'
line_length=int(sys.stdin.readline())
for _ in range(line_length):
    line=sys.stdin.readline().rstrip()
    print(solution(line))
