from collections import defaultdict
def solution(id_list, report, k):
    report=list(set(report))
    count={id: [] for id in id_list}
    answerdic={id: 0 for id in id_list}
    answer = set()
    
    for rep in report:
        a=rep.split(' ')
        reportUser=a[0]
        reportedUser=a[1]
        count[reportedUser].append(reportUser)
        if(len(count[reportedUser])>=k):
            answer.add(reportedUser)
    for reportedUser in answer:
        for user in count[reportedUser]:
            answerdic[user]+=1
    return list(answerdic.values())