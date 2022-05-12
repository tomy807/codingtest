num=str(input())
arr=list(map(int,num))
arr.sort(key=lambda x:-x)
print(int(''.join(map(str,arr))))
