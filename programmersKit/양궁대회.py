from collections import deque
def bfs(n,info):
    res=[]
    queue=deque([(0,[0 for _ in range(11)])])
    while queue:
        focus,ApacheBoard=queue.popleft()
        cntApache=sum(ApacheBoard)
        # 화살을 다 쏨
        if cntApache==n:
            pass
        # 화살을 더 쏘면 없앰
        elif cntApache>n:
            continue
        # 화살을 덜 쏨 근데 끝->화살 다 소비
        elif focus==10:
            pass
        # 화살을 쏘는 단계(라이언보다 1개 더 쏘거나 안쏘거나)
        else:
            tmp1=ApacheBoard.copy()
            tmp1[focus]=info[focus]+1
            q.append((focus+1,tmp1))
            
            tmp2=ApacheBoard.copy()
            tmp2[focus]=0
            q.append((focus+1,tmp2))

def solution(n, info):
    overScore=[i+1 for i in info]
    answer = []
    return overScore
n=5
info=[2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))