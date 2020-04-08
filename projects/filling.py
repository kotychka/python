name = input("Write your name here: ")
quant = 14
if ( len(name) - quant ) % 2 != 0:
	quant += 1

print('{0:*^{1}}' .format (name, quant))


# Antother way of solving
# if ( len(name) % 2 ):
# 	quant +=1

# print( ('{0:*^'+str(quant)+'}') .format (name) )