from itertools import combinations

N,M= map(int,input().split(' '))
nums=list(map(int,input().split(' ')))
nums.sort()
for i in combinations(nums, M):
    print(' '.join(map(str,i)))


# N, M = map(int, input().split())
# L = list(map(int, input().split()))
# L.sort()
# visited = [False] * N
# out = []
# def solve(depth, idx, N, M):
#     if depth == M:
#         print(' '.join(map(str, out)))
#         return
#     for i in range(idx, N):
#         if not visited[i]:
#             visited[i] = True
#             out.append(L[i])
#             solve(depth+1, i+1, N, M)
#             out.pop()
#             visited[i] = False

# solve(0, 0, N, M)