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