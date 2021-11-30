from collections import deque

def check(queue):
    stack=[]
    while queue:
        qu=queue.popleft()
        if qu in ('{','[','('):
            stack.append(qu)
        else:
            if not stack:
                return False
            out=stack.pop()
            if qu=='}' and out!='{':
                return False
            elif qu==']' and out!='[':
                return False
            elif qu==')' and out!='(':
                return False    
    if len(stack) !=0:
        return False
    return True

def solution(s):
    answer=0
    for i in range(len(s)):
        queue=deque(s)
        queue.rotate(-i)
        if check(queue):
            answer+=1
    return answer
print(solution("[](){}"))