import sys
import itertools
usingNumbers,lenght = map(int,sys.stdin.readline().split())
numberlist=[str(i) for i in range(1,usingNumbers+1)]
results=list(map(' '.join,itertools.combinations(numberlist,lenght)))
for result in results:
    print(result)
