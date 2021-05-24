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
# from sympy import *
# import numpy 
# import itertools
# x1=Symbol('x1')
# x2=Symbol('x2')
# x3=Symbol('x3')
# x4=Symbol('x4')
# x5=Symbol('x5')
# x6=Symbol('x6')
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
# A=Matrix([[1,0,1],[0,0,2],[-1,-1,2]])
# B=Matrix([[-1,0,1],[0,-1,1],[0,0,2]])
# C=Matrix([6,8,4])
# D=Matrix([x4,x5,x2])
# D1=Matrix([x1,x6,x3])
# Ainv=A.inv()
# E=Ainv*C
# F=Ainv*B*D
# print(Ainv)
# print(E)
# print(Ainv*B)
# print(F)
# print(E-F)
# D1=E-F
# print(D1)
# equ=2*D1[0]+10*x2+8*D1[2]
# print(equ)
# a='((()))'
# n=a.translate({ord('('):')',ord(')'):'('})
# print(n)
# if "":
#     print("abcd")
# else:
#     print("dnaid")
# str2="abcde"
# str1="abczolw"
# str_set=set(str2)
# str_set1=set(str1)
# a=str_set-str_set1
# print(a)
# import itertools
# a={'A', 'D', 'E'}
# b=list(map(set,itertools.combinations(a, 2)))
# print(list(b)[0])
# import re
# a="- and - and - and chicken 100"
# b=a.replace('and','').split()
# # b=b.split()
# c="java backend junior pizza 150"
# d=c.split()
# print(b)
# print(d)
# a=[]
# str_1='1234'
# str_2=str_1+'가너다'
# a.append(str_2)
# print(a)
# i=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# a="Enter uid1234 Muzi"
# print(a.split())
# z,x,y="Enter uid1234 Muzi".split()
# print(y)
# print(["Prodo님이 들어왔습니다.","Ryan님이 들어왔습니다.","Prodo님이 나갔습니다.","Prodo님이 들어왔습니다."]==['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다', 'Prodo님이 들어왔습니다.'])
# matrix=[[i+j*3 for i in range(1,4)] for j in range(4)]
# print(matrix)
# from collections import defaultdict
# dic=defaultdict(list)
# dic[1].append(2)
# dic[2]=1
# li=[]
# li.append(1)
# print(dic)
# k=[1,2,3,4]
ground=[[0 for _ in range(2)] for _ in range(7)]
print(ground[6][1])
# a=[[1,2],[2,3]]
# print([1,2] not in a)
# import sys
# maze=[]
# for _ in range(2):
#     y=list(map(int,list(sys.stdin.readline().strip())))
#     maze.append(y) 
# print(maze)