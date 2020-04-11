import math 

def greatest_product(n):
	prod = 0
	length = len(n) - 5
	leng = len(n)
	# n = int(n)
	n = list(n)
	leng = len(n)
	i = 0
	for i in leng:
		print(n[i])
		# n[i] = int(n[i])

	print(n)
	while i <= length:
		print(n[i:i+5])
		i+=1
		# prod2 = math.prod(int(n[i:i+5])
		# print(prod2)

		# if new_prod > prod:
			# prod = new_prod
	print(prod)

greatest_product("123834539")