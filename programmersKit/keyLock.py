import pprint



def rotation90(key):
    for i in range(4):
        new_key=[k[::-1] for k in zip(*key)]
    return new_key

def move(key,lock,starty,startx):
    M=len(key)
    keyBoard=[[-1 for _ in range(3*M)] for _ in range(3*M)]
    for i in range(M):
        for j in range(M):
            keyBoard[starty+i][startx+j]=key[i][j]
    keyBoard=[row[M:2*M] for row in keyBoard[M:2*M]]
    for i in range(M):
        for j in range(M):
            if keyBoard[i][j]+lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    M=len(key)
    N=len(lock)
    answer = True
    for _ in range(4):
        key=rotation90(key)
        for starty in range(1,2*M+1):
            for startx in range(1,2*M+1):
                answer=move(key,lock, starty, startx)
                if answer==True:
                    return True
    return False
                
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])) 