# def solution(p):
#     answer = ''
#     countleft=0
#     couuntright=0
#     for i in p:
#         if i=='(':
#             countleft+=1
#         else:
#             couuntright+=1
#         if couuntright==countleft:
#             frag=
#     return answer
# def solution(p):
#     u=rightorder(p[0:balanced(p)])
#     v=p[balanced((p)):]
#     return u+solution(v)
    
# def balanced(p):
#     countleft=0
#     couuntright=0
#     for i in p:
#         if i=='(':
#             countleft+=1
#         else:
#             couuntright+=1
#         if couuntright==countleft:
#             return countleft+couuntright
# def balanced(p):
#     countleft=0
#     couuntright=0
#     for i in p:
#         if i=='(':
#             countleft+=1
#         elif i==')':
#             couuntright+=1
#         if couuntright==countleft:
#             return countleft+couuntright
from collections import deque
def detach(s):
    str_dq=deque(s)
    u=""
    v=""
    countleft=0
    couuntright=0
    while str_dq:
        u+=str_dq.popleft()
        if u[-1]=='(':
            countleft+=1
        else:
            couuntright+=1
        if countleft==couuntright:
            break
    v=''.join(list(str_dq))
    return u,v
def is_correct(string):  # 올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return not stack
def reverse(u):  # 뒤집기
    return ''.join([')' if s == '(' else '('for s in u])
def recursion(s):
    if s=='':
        return ''
    u,v=detach(s)
    if is_correct(u):
        return u+recursion(v)
    else:
        return '('+recursion(v)+')'+reverse(u[1:-1])
    
print(recursion('()))((()'))