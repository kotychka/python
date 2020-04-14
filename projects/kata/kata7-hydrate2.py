def hydrate(drink_string): 
    # your code here
    drink_sum = 0
    for i in drink_string:
    	if i.isnumeric():
            drink_sum += int(i)
    if drink_sum == 1:
    	return "1 glass of water"
    else:
    	return str(drink_sum) + " glasses of water"

print(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"))
print(hydrate("1 beer"))
    