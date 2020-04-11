# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

def square_digits(num):
    new_num = ''
    for elem in str(num):
    	new_num += str(int(elem)**2)
    print(int(new_num))

square_digits(9119)		# 811181 