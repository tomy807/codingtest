import sys 
num=int(sys.stdin.readline())
N=[]*100
n=['1','2','3','4','5','6','7','8','9']
N.append(n)
for j in range(num):
    for n in N:
        li=[]
        for i in n:
            if i=='1':
                li.append(i+str(0))
                li.append(i+str(2))
            if not (int(i[0])==1 or int(i[-1])==0 or int(i[-1])==9):
                li.append(i+str(int(i)+1))
                li.append(i+str(int(i)-1))
                li.append(str(int(i)+1)+i)
                li.append(str(int(i)-1)+i)
            else:
                if int(i[0])==1:
                    li.append(str(int(i)+1)+i)
                if int(i[-1])==0:
                    li.append(i+str(int(i)+1))
                if int(i[-1])==9:
                    li.append(i+str(8))
    N.append(list(set(li)))
print(N)