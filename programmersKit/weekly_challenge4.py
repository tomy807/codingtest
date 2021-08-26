def solution(table, languages, preference):
    newtable=[]
    result=[]
    for jobPoints in table:
        newtable.append(jobPoints.split())
    for points in newtable:
        sumPoint=0
        for language in languages:
            if language in points:
                sumPoint+=(6-points.index(language))*preference[languages.index(language)]
        result.append((points[0],sumPoint))
    result.sort(key=lambda x:(-x[1],x[0]))
    return result[0][0]
solution(table, languages, preference)