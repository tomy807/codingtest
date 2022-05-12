import sys

T=int(input())
for test in range(T):
    N=int(input())
    cards=list(map(int,sys.stdin.readline().split(' ')))
    cards.sort()
    evenCards=[]
    oddCards=[]
    for card in cards:
        if card%2==0:
            evenCards.append(card)
        else:
            oddCards.append(card)  
    print(evenCards)
    print(oddCards)
    

