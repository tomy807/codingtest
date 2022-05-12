import sys
N=int(sys.stdin.readline())
arr=[]
arr_dict=dict()
for _ in range(N):
    num=int(sys.stdin.readline())
    arr.append(num)
    if num in arr_dict.keys():
        arr_dict[num]+=1
    else:
        arr_dict[num]=1
arr.sort()
MaxNum=max(arr_dict.values())
MaxNumArr=[]
for i in arr_dict.keys():
    if arr_dict[i]==MaxNum:
        MaxNumArr.append(i)
MaxNumArr.sort()
print(round(sum(arr)/N))
print(arr[N//2])
if len(MaxNumArr)>=2:
    print(MaxNumArr[1])
else:
    print(MaxNumArr[0])
print(max(arr)-min(arr))