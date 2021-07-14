import sys

def solution(line):
    vps_list=[]
    for alp in line:
        if(alp in ('(',')','[',']')):
            vps_list.append(alp)
    return vps_list

def checking(vps_list):
    stack=[]
    for vps in vps_list:
        if(vps=='('or vps=='['):
            stack.append(vps)
        else:
            if(len(stack)==0):
                return False
            else:
                out=stack[-1]
                if(vps==')' and out=='('):
                    stack.pop()
                elif(vps==']' and out=='['):
                    stack.pop()
                else:
                    return False
    if(len(stack)>0):
        return False
    else:
        return True
while(True):
    line=sys.stdin.readline().rstrip()
    if(line=='.'):
        break
    vps_list=solution(line)
    if(checking(vps_list)):
        print("Yes")
    else:
        print("NO")
    