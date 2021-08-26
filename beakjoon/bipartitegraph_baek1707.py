import sys
from collections import defaultdict
from collections import deque

def bfs(start):
    queue=deque()
    queue.append(start)
    edge_color[start]=1
    while queue:
        now_edge=queue.popleft()
        for next_edge in graph_dict[now_edge]:
            if edge_color[next_edge] ==0:
                edge_color[next_edge]=-edge_color[now_edge]
                queue.append(next_edge)
            else:
                if edge_color[next_edge]==edge_color[now_edge]:
                    return False
    return True


test=int(sys.stdin.readline())
for _ in range(test):
    Edge,Line= map(int, sys.stdin.readline().split())
    graph_dict=defaultdict(list)
    edge_color=[0]*(Edge+1)
    isTrue=True
    for _ in range(Line):
        edge1,edge2=map(int, sys.stdin.readline().split())
        graph_dict[edge1].append(edge2)
        graph_dict[edge2].append(edge1)
    for start in range(1,Edge+1):
        if edge_color[start]==0:
            if not bfs(start):
                isTrue = False
                break
    print("YES" if isTrue else "NO")