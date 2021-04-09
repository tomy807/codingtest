import collections
a=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
b=[[i for i in range(5)]for _ in range(5)]
b[3][2]=100
c=[]
print(b)
mylist=list(map(list,zip(*a)))
print(mylist)
deq=collections.deque(mylist)
deq.popleft()
print(deq)
print(mylist)
dqlist=[]
print(dqlist)
for i in range(5):
    deq=collections.deque(mylist[i])
    dqlist.append(deq)
print(dqlist)  
dqlist[1].popleft()
print(type(a))
print(dqlist)
answer=0
stack=[]
collect=[1,2,3,4,5]
it=iter(collect)    #iter next 이용해보기
while True:
    try: 
        data=next(it)
        print(data)
    except StopIteration:
        print("end")
        break
collect_dq=collections.deque(collect)
a=collect_dq.popleft()
stack.append(a)
while collect_dq:
    b=collect_dq.popleft()
    if stack:
        if stack[-1]==b:
            stack.pop()
            answer=answer+2
        else:
            stack.append(b)
    else:
        stack.append(b)
print(answer)
from itertools import combinations
items=[1,2,3,4,5]
z=list(map(lambda x:x[0]+x[1],combinations(items,2))) 
print(list(set(z)))
akowk="aBc_&^&*_"
import string
def listAlphabet():
  return list(string.ascii_lowercase)
alp=list(string.ascii_lowercase)
print('a' in alp)
stralp="abcdeks"
for i in range((len(stralp))):
    print(i)
    print(stralp[i])
print(akowk.lower())
qwer='.........abcdsed.........'
qw='1223'
qwer=qwer.strip('.')
print(qwer)
ten=45
three=[]
while True:
    three.append(ten%3)
    ten=ten//3
    if ten<3:
        three.append(ten)
        break
print(three)
print(3^5)