def solution(record):
    answer = []
    id_dict={}
    for i in record:
        if i.split()[0]=='Enter':
            id_dict[i.split()[1]]=i.split()[2]
        if i.split()[0]=='Leave':
            pass
        if i.split()[0]=='Change':
            id_dict[i.split()[1]]=i.split()[2]
    for j in record:
        if j.split()[0]=='Enter':
            answer.append("{}님이 들어왔습니다.".format(id_dict[j.split()[1]]))
        if j.split()[0]=='Leave':
            answer.append("{}님이 나갔습니다.".format(id_dict[j.split()[1]]))
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# ["Prodo님이 들어왔습니다.","Ryan님이 들어왔습니다.","Prodo님이 나갔습니다.","Prodo님이 들어왔습니다."]
# ['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다', 'Prodo님이 들어왔습니다.']