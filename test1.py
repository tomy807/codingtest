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
collect=[1,1,1,1,1]
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