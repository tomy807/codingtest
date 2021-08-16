def solution(price, money, count):

    total_price=price*(1+count)*count/2
    answer=total_price-money
    if answer<=0:
        return 0
    else:
        return int(answer)
print(solution(3, 20, 4))