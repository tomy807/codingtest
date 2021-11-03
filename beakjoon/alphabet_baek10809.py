import sys
from string import ascii_lowercase
answer=''
word=str(sys.stdin.readline().strip())
alphabet=list(ascii_lowercase)
for i in alphabet:
    if i in word:
        answer+=str(word.index(i))+' '
    else:
        answer+='-1 '
print(answer.rstrip())
