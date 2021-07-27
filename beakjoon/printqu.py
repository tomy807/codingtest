import sys
test=int(sys.stdin.readline())
for _ in range(test):
    print_length,point=map(int,sys.stdin.readline().split(' '))
    s=list(map(int,sys.stdin.readline().split(' '))) 
    count=0
    s_=[0 for _ in range(print_length)] 
    s_[point]=1
    while True:
        if s[0]==max(s):
            count+=1
            if s_[0]==1:
                print(count)
                break
            else:
                del s[0]
                del s_[0]
        else:
            s.append(s[0])
            del s[0]
            s_.append(s_[0])
            del s_[0]
        
