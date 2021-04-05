def solution():
    a=[0]*100
    sums=[0]*100
    cnt=0
    cnt3=0
    n=int(input("총 개수를 쓰시오"))
    for i in range(n):
        a[i]=int(input("입력하세요"))
        print(str(i+1)+"번째 수는"+str(a[i])+"입니다.")
    sums[0]=a[0]
    for i in range(n):
        sums[i+1]=a[i+1]+sums[i]
    total=sums[n-1]
    total3=total/3
    if total%3!=0:
        return 0
    else:
        if a[0]==total3:
            cnt3+=1
        for i in range(n):
            if a[i]==total3*2:
                cnt+=cnt3
            if a[i]==total3:
                cnt+=1
    return cnt
print(solution())


