def solution(scores):
    new_list = list(map(list, zip(*scores)))
    list_lenght = len(new_list[0])
    avg_point=0
    answer=''
    for i in range(list_lenght):
        max_list=max(new_list[i])
        min_list=min(new_list[i])
        if new_list[i].count(max_list)==1 and new_list[i][i]==max_list :
            del new_list[i][i]
        elif new_list[i].count(min_list)==1 and new_list[i][i]==min_list:
            del new_list[i][i]
        avg_point=sum(new_list[i])/len(new_list[i])
        answer+=checkpoint(avg_point)
        print(new_list[i])
        print(avg_point)
    return answer

def checkpoint(avg_point):
    if avg_point>=90:
        return 'A'
    elif 80 <=avg_point <90:
        return 'B'
    elif 70 <=avg_point <80:
        return 'C'
    elif 50 <=avg_point <70:
        return 'D'
    else:
        return 'F'
print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))