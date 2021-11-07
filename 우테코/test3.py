def solution(ings, menu, sell):
    ingsdict={}
    menudict={}
    result=0
    for ing in ings:
        ing_name,ing_price=ing.split(' ')
        ingsdict[ing_name]=int(ing_price)
    for food in menu:
        food_name,fooding_price,food_price=food.split(' ')
        fooding_total_price=0
        fooding_price_set=set(fooding_price)
        for i in fooding_price_set:
            fooding_total_price+=fooding_price.count(i)*ingsdict[i]
        menudict[food_name]=int(food_price)-fooding_total_price
    for out in sell:
        out_name,out_count=out.split(' ')
        result+=menudict[out_name]*int(out_count)
    return result

print(solution(["x 25", "y 20", "z 1000"], 
               ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"], 
               ["BBBB 3", "TTT 2"]))