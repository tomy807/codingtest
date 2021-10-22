# global parent
# def find(x):
#     if x==parent[x]:
#         return x
#     else:
#         parent[x]=find(parent[x])
#         return parent[x]
# def merge(x,y):
#     x=find(x)
#     y=find(y)
#     if x<y:
#         parent[y]=x 
#     else:
#         parent[x]=y
# def solution(n, wires):
#     global parent
#     result=[]
#     for i in range(len(wires)):
#         parent=[i for i in range(n+1)]
#         for j in range(len(wires)):
#             if i!=j:
#                 merge(wires[j][0], wires[j][1])
#         new_parent=parent[1:]
#         new_parent_set=list(set(new_parent))
#         result.append(abs(new_parent.count(new_parent_set[0])-new_parent.count(new_parent_set[1])))
#         print(new_parent)
#     return new_parent
# print(solution(6,[[1,2],[5,6],[3,4],[4,5],[2,3]]))
from collections import defaultdict
global dic
def solution(n, wires):
    global dic
    result=[]
    for i in range(len(wires)):
        dic=defaultdict(list)
        for j in range(len(wires)):
            if i!=j:
                dic[wires[j][0]].append(wires[j][1])
                dic[wires[j][1]].append(wires[j][0])
        lendfs=dfs(1)
        result.append(abs((n-lendfs)-lendfs))
    return min(result)

def dfs(start):
    stack=[]
    visited=[]
    stack.append(start)
    while stack:
        out=stack.pop()
        if out not in visited:
            visited.append(out)
            for value in tmp:
                if value in visited:
                    continue
                else:
                    stack.append(value)
    return len(visited)
print(solution(6,[[1,2],[5,6],[3,4],[4,5],[2,3]]))