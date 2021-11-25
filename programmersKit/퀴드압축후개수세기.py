def solution(arr):
    answer = [0,0]

    def rec(a,b,n):
        number=arr[a][b]
        for i in range(a,a+n):
            for j in range(b,b+n):
                if arr[i][j]!=number:
                    nn=n//2
                    rec(a, b, nn)
                    rec(a+nn, b, nn)
                    rec(a, b+nn, nn)
                    rec(a+nn, b+nn, nn)
                    return
        answer[number]+=1
    
    rec(0, 0, len(arr))
    return answer
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))