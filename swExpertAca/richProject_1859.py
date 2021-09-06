import sys

tests=int(input())
for test in range(tests):
    days_lenght=int(input())
    prices = list(map(int,input().split()))
    max_price=prices[days_lenght-1]
    total_price=0
    for day in range(days_lenght-2,-1,-1):
        if max_price>prices[day]:
            total_price+=max_price-prices[day]
        else:
            max_price=prices[day]
    print("#{} {}".format(test+1,total_price))
