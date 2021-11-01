from itertools import permutations
def solution(expression):
    Multiple='*'
    Plus='+'
    Minus='-'
    operations=list(permutations([Multiple,Plus,Minus],3))
    answer = []
    splitExpression=[]
    count=0
    for i in range(len(expression)):
        if expression[i] in('*','-','+'):
            splitExpression.append(expression[i-count:i])
            splitExpression.append(expression[i])
            count=0
        else:
            count+=1
    splitExpression.append(expression[-count:])
    for operation in operations:
        newsplitExpression=splitExpression
        for oper in operation:
            if oper=='*':
                while('*' in newsplitExpression):
                    index=newsplitExpression.index('*')
                    newExpression=newsplitExpression[:index-1]
                    newExpression.append(int(newsplitExpression[index-1])*int(newsplitExpression[index+1]))
                    newExpression.extend(newsplitExpression[index+2:])
                    newsplitExpression=newExpression
            elif oper=='-':
                while('-' in newsplitExpression):
                    index=newsplitExpression.index('-')
                    newExpression=newsplitExpression[:index-1]
                    newExpression.append(int(newsplitExpression[index-1])-int(newsplitExpression[index+1]))
                    newExpression.extend(newsplitExpression[index+2:])
                    newsplitExpression=newExpression
            else:
                while('+' in newsplitExpression):
                    index=newsplitExpression.index('+')
                    newExpression=newsplitExpression[:index-1]
                    newExpression.append(int(newsplitExpression[index-1])+int(newsplitExpression[index+1]))
                    newExpression.extend(newsplitExpression[index+2:])
                    newsplitExpression=newExpression
        answer.append(abs(newsplitExpression[0]))
    return max(answer)
print(solution("100-200*300-500+20"))