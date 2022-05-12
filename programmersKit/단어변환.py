def solution(begin, target, words):
    answer=100000
    if target not in words:
        answer=0
    answer=dfs(begin, target, words)
    return answer
def dfs(begin, target, words):
    depth=0
    visited={word:0 for word in words}
    stack=set()
    stack.add(begin)
    while stack:
        out=stack.pop()
        if(out==target):
            return depth
        visited[out]=1
        depth+=1
        for word in words:
            count=0
            targetCount=0
            if visited[word]==0:
                for i in range(len(word)):
                    if word[i]==out[i]:
                        count+=1
                if(count==len(word)-1):
                    stack.add(word)
    print(depth)
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))