while True:
    try:
        x = int(input())
    except EOFError:
        break
    if x==1:
        print(1)
        break
    num=1
    answer=1
    while True:
        num=10*num+1
        answer+=1
        if num%x==0:
            print(answer)
            break