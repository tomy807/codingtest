# def solution(s):
#     answer = 0
#     count=1
#     count_list1=[]
#     count_list=[]
#     lenght=len(s)
#     s_list=[]
#     for i in range(1,lenght//2+1):
#         s_list.append([s[j:j+i] for j in range(0,len(s),i)])
#     for i in s_list:
#         count_list=[]
#         for j in range(len(i)):
#             try:
#                 if i[j]==i[j+1]:
#                     count+=1
#                 else:
#                     count_list.append(count)
#                     count=1
#             except IndexError:
#                 count_list.append(1)
#         count_list1.append(count_list)
#     print(s_list)
#     return count_list1
# print(solution("aabbaccc"))
# x = iter([1,2,3,4,5,6,7,8,9])
# print(list(zip(x, x, x)))
# a=[1,2,3]
# b=[4,5,6]
# c=zip(a,b)
# x=iter([1,2,3,4,5,6,7])
# print(list(zip(x,x)))
# print(list(x),list(x))
def solution(s):
    lenght=len(s)
    answer=[]
    result=''
    if lenght==1:
        return 1
    for cut in range(1,lenght//2+1):
        temp=s[:cut]
        count=1
        for i in range(cut,lenght,cut):
            if temp==s[i:cut+i]:
                count+=1
            else:
                if count==1:
                    result+=temp
                else:
                    result+=str(count)+temp
                count=1
            temp=s[i:cut+i]
        if count==1:
            count=""
        result+=str(count)+temp
        answer.append(len(result))
        result=''
    answer.append(lenght)
    return min(answer)
print(solution("ababcdcdababcdcd"))


