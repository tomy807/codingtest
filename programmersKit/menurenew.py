import itertools
def intersec(a):
    return a[0].intersection(a[1])
def solution(orders, course):
    answer = []
    set_list=[]
    for i in orders:
        set_list.append(set(i))
    a=list(map(intersec,itertools.combinations(set_list, 2)))
    new_list=[]
    new_list1=[]
    for i in a:
        if  len(i) in course and len(i)==2:
            new_list.append(i)
        if len(i) in course and len(i)>2:
            for j in range(2,len(i)+1):
                if j in course:
                    new_list.extend(list(map(set,itertools.combinations(i, j))))
    for i in new_list:
        tmp=list(i)
        tmp.sort()
        tmp=''.join(tmp)
        new_list1.append(tmp)
    new_list1.sort()
    counter={}
    for i in new_list1:
        if i not in counter:
            counter[i]=[0,len(i)]
        counter[i][0]+=1
    value_list=list(counter.values())
    lenght_list=[]
    for i in new_list1:
        if len(i) not in lenght_list:
            lenght_list.append(len(i))
    for j in lenght_list:
        maxi=0
        for k in value_list:
            if k[1]==j:
                if k[0]>maxi:
                    maxi=k[0]
    return new_list1
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
