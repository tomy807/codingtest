import collections
import string
import re
def solution(new_id):
    new_id1=re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    dq=collections.deque(list(new_id1))
    new_id2=[]
    if dq:
        a=dq.popleft()
        new_id2.append(a)
        while dq:
            b=dq.popleft()
            if new_id2[-1]=='.' and b=='.':
                continue
            else:
                new_id2.append(b)
    new_id2="".join(new_id2)
    if new_id2:
        new_id2=new_id2.strip('.')
    if not new_id2:
        new_id2=new_id2+'a'
    new_id2=new_id2[:15]
    if new_id2:
        new_id2=new_id2.strip('.')
    if not new_id2:
        new_id2=new_id2+'a'
    if len(new_id2)==1:
        tmp=str(new_id2[-1])
        new_id2=new_id2+tmp
        new_id2=new_id2+tmp
    if len(new_id2)==2:
        tmp=str(new_id2[-1])
        new_id2=new_id2+tmp
    return new_id2
print(solution("......a......a......a....."))


import re
def solution(new_id):
    answer = ''
    # 1단계 & 2단계 : 소문자 치환
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    # 3단계 : 마침표 2번 이상 > 하나로
    answer = re.sub('\.\.+', '.', answer)
    # 4단계 : 양 끝 마침표 제거
    answer = re.sub('^\.|\.$', '', answer)
    # 5단계 : 빈 문자열이면 a 대입
    if answer == '':
        answer = 'a'
    # 6단계 : 길이가 16자 이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])
    # 7단계 : 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(answer) < 3:
        answer += answer[-1:]
    return answer