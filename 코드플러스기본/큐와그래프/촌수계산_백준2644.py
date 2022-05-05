from collections import deque
n = int(input())
start, target = map(int, input().split())
m = int(input())
bloodCnt = [[] for _ in range(n+1)]
check = [0]*(n+1)
for _ in range(m):
    parent, child = map(int, input().split())
    bloodCnt[parent].append(child)
    bloodCnt[child].append(parent)
queue = deque([start])
while queue:
    out = queue.pop()
    for i in bloodCnt[out]:
        if check[i] == 0:
            check[i] = check[out]+1
            queue.append(i)
if check[target] == 0:
    print(-1)
else:
    print(check[target])
