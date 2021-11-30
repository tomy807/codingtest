import re
def solution(info, query):
    answer = []
    info_1=[]
    query_1=[]
    for i in info:
        info_1.append(i.split())
    for j in query:
        q=j.replace('and','').split()
        count=0
        query_1.append(q)
        # for t in info_1:
        #     if not int(t[4])>=int(q[4]):
        #         continue
        #     else:
        #         if (q[0]==t[0] or q[0]=='-') and (q[1]==t[1] or q[1]=='-') and (q[2]==t[2] or q[2]=='-') and (q[3]==t[3] or q[3]=='-') :
        #             count+=1
        # answer.append(count)
    print(info_1)
    print(query_1)


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
 ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))