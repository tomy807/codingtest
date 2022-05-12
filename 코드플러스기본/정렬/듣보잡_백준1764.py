import sys
N,M=map(int,sys.stdin.readline().split())
dbj=set()
people=[]
answer=[]
for _ in range(N):
    dbj.add(sys.stdin.readline().rstrip())
for _ in range(M):
    people.append(sys.stdin.readline().rstrip())
for person in people:
    if person in dbj:
        answer.append(person)
answer.sort()
print(len(answer))
for i in answer:
    print(i)