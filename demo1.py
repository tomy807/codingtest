def solution(registered_list, new_id):
    while new_id in registered_list:
        new_id=recommend(new_id)
    return new_id

def recommend(new_id):
    cnt=0
    eng=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','w','z']
    for element in new_id:
        cnt+=1
        if element not in eng:
            S=new_id[0:cnt-1]
            N=int(new_id[cnt-1:])
            return S+str(N+1)        
    return new_id+str(1)

print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))