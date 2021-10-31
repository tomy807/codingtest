from itertools import permutations

def solution(k, dungeons):
    answer = []
    dungeons=list(permutations(dungeons,len(dungeons)))
    for dungeon in dungeons:
        count=0
        newK=k
        for minTired,tired in dungeon:
            if newK<minTired:
                continue
            else:
                newK=newK-tired
                count+=1
        answer.append(count)
    return max(answer)

print(solution(80,[[80,20],[50,40],[30,10]]))