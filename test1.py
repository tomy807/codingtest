# import collections
# a=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# b=[[i for i in range(5)]for _ in range(5)]
# b[3][2]=100
# c=[]
# print(b)
# mylist=list(map(list,zip(*a)))
# print(mylist)
# deq=collections.deque(mylist)
# deq.popleft()
# print(deq)
# print(mylist)
# dqlist=[]
# print(dqlist)
# for i in range(5):
#     deq=collections.deque(mylist[i])
#     dqlist.append(deq)
# print(dqlist)  
# dqlist[1].popleft()
# print(type(a))
# print(dqlist)
# answer=0
# stack=[]
# collect=[1,2,3,4,5]
# it=iter(collect)    #iter next 이용해보기
# while True:
#     try: 
#         data=next(it)
#         print(data)
#     except StopIteration:
#         print("end")
#         break
# collect_dq=collections.deque(collect)
# a=collect_dq.popleft()
# stack.append(a)
# while collect_dq:
#     b=collect_dq.popleft()
#     if stack:
#         if stack[-1]==b:
#             stack.pop()
#             answer=answer+2
#         else:
#             stack.append(b)
#     else:
#         stack.append(b)
# print(answer)
# from itertools import combinations
# items=[1,2,3,4,5]
# z=list(map(lambda x:x[0]+x[1],combinations(items,2))) 
# print(list(set(z)))
# akowk="aBc_&^&*_"
# import string
# def listAlphabet():
#   return list(string.ascii_lowercase)
# alp=list(string.ascii_lowercase)
# print('a' in alp)
# stralp="abcdeks"
# for i in range((len(stralp))):
#     print(i)
#     print(stralp[i])
# print(akowk.lower())
# qwer='.........abcdsed.........'
# qw='1223'
# qwer=qwer.strip('.')
# print(qwer)
# ten=45
# three=[]
# while True:
#     three.append(ten%3)
#     ten=ten//3
#     if ten<3:
#         three.append(ten)
#         break
# print(three)
# print(3^5)
# from collections import Counter
# lis1=[1,2,3,4,2,3,4]
# dic=Counter(lis1)
# print(dic)
# print(dic.values)    x+y+z-6   y+z-8   -x+2*y+2*z-4
from sympy import *
import numpy 
import itertools
x1=Symbol('x1')
x2=Symbol('x2')
x3=Symbol('x3')
x4=Symbol('x4')
x5=Symbol('x5')
x6=Symbol('x6')
# equation1= x1+x2+x3-6
# equation2= x2+2*x3-8
# equation3= -x1+2*x2+2*x3-4
# equation4= x1
# equation5= x2
# equation6= x3
# equlist=[equation1,equation2,equation3,equation4,equation5,equation6]
# for a,b,c in itertools.combinations(equlist, 3):
#     d=solve((a,b,c),dict=True)
#     print(d[0]+d[1]+d[2]-6)
#     print(x2+2*x3-8)
#     print(-x1+2*x2+2*x3-4)
# print(solve((equation1,equation2,equation3),dict=True))
# print(solve([]))
A=Matrix([[1,0,1],[0,0,2],[-1,-1,2]])
B=Matrix([[-1,0,1],[0,-1,1],[0,0,2]])
C=Matrix([6,8,4])
D=Matrix([x4,x5,x2])
D1=Matrix([x1,x6,x3])
Ainv=A.inv()
E=Ainv*C
F=Ainv*B*D
print(Ainv)
print(E)
print(Ainv*B)
print(F)
print(E-F)
D1=E-F
print(D1)
equ=2*D1[0]+10*x2+8*D1[2]
print(equ)