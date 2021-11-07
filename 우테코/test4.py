from collections import deque
def solution(s):
    queue=deque(s)
    count=1
    answer = []
    while queue:
        out=queue.popleft()
        if queue:
            if out==queue[0]:
                count+=1
            else:
                answer.append(count)
                count=1
        elif out==s[0]:
            answer[0]+=count
        else:
            answer.append(count)
    answer.sort(reverse=False)
    return answer
print(solution("wowwow"))