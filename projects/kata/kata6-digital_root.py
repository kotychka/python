# digital_root(493193)
# => 4 + 9 + 3 + 1 + 9 + 3
# => 29 ...
# => 2 + 9
# => 11 ...
# => 1 + 1
# => 2

def digital_root(n):
	list_s = []
	s = 0
	while n // 10 >0:
		s = n%10
		n = n//10
		list_s.append(s)
	list_s.append(n%10)
	list_s.reverse()
	if sum(list_s) < 10:
		list_s = [sum(list_s)]
	else:
		while sum(list_s) >= 10:
			list_s = [sum(list_s)%10+sum(list_s)//10]
	print(list_s[0])

digital_root(16) #7
digital_root(456) #6
digital_root(493193) #2


### Not mine solution
# def digital_root(n):
#     while n>10:
#         n = sum([int(i) for i in str(n)])
#     return n

## Not mine solution2
# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))

## Not mine solution3
# def digital_root(n):
#     return n%9 or n and 9 