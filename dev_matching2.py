def solution(n, recipes, orders):
    recipes_dict={}
    answer = 0
    cookingFires=[0 for _ in range(n)]
    for recipe in recipes:
        c,d=recipe.split(' ')
        recipes_dict[c]=int(d)
    for order in orders:
        menu=order.split(' ')[0]
        order_time=int(order.split(' ')[1])
        print(menu,order_time)
        for i in range(n):
            print(cookingFires)
            if cookingFires[i]<=order_time:
                cookingFires[i]+=(recipes_dict[menu]+order_time)
                break
                
    return cookingFires
print(solution(2, ["A 3","B 2"], ["A 1","A 2","B 3","B 4"]))

# 2	["A 3","B 2"]	["A 1","A 2","B 3","B 4"]	7
# 3	["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"]	["PIZZA 1", "FRIEDRICE 2", "SPAGHETTI 4", "SPAGHETTI 6", "PIZZA 7", "SPAGHETTI 8"]	12
# 1	["COOKIE 10000"]	["COOKIE 300000"]	310000

