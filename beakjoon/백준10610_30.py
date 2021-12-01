nums=list(map(int, str(input())))
if sum(nums)%3==0 and 0 in nums:
    nums.sort(reverse=True)
    print(''.join(str(_) for _ in nums))
else:
    print(-1)