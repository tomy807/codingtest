N=int(input())
nums=list(map(int, input().split(' ')))
nums.sort()
sums=0
print(nums)
# allPart=[]
# def dfs(s,depth):
#     if depth==N:
#         allPart.append(s)
#         return
#     s+=nums[depth]
#     dfs(s, depth+1)
#     dfs(s-nums[depth], depth+1)
# dfs(0, 0)
# allPart=set(allPart)
# for i in range(1,2000000):
#     if i not in allPart:
#         print(i)
#         break
for i in range(N):
    if nums[i]>(sums+1):
        break
    sums+=nums[i]
print(sums+1)