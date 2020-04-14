def hydrate(drink_string): 
    # your code here
    point0 = drink_string.count(' ')+drink_string.count(',')
    point1 = point0 + drink_string.count(',') + 1
    numbers = sorted(drink_string)[point0:point1]
    drink_sum = 0
    for i in numbers:
    	drink_sum += int(i)
    if drink_sum == 1:
    	return str(drink_sum) + " glass of water"
    else:
    	return str(drink_sum) + " glasses of water"

print(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"))
print(hydrate("1 beer"))

# assert hydrate("1 beer") == "1 glass of water"
# assert hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer") == "10 glasses of water"