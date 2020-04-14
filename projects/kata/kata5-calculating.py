def zero(oper=''): return 0 if oper=='' else operation(0, oper)
def one(oper=''): return 1 if oper=='' else operation(1, oper)
def two(oper=''): return 2 if oper=='' else operation(2, oper)
def three(oper=''): return 3 if oper=='' else operation(3, oper)
def four(oper=''): return 4 if oper=='' else operation(4, oper)
def five(oper=''): return 5 if oper=='' else operation(5, oper)
def six(oper=''): return 6 if oper=='' else operation(6, oper)
def seven(oper=''): return 7 if oper=='' else operation(7, oper)
def eight(oper=''): return 8 if oper=='' else operation(8, oper)
def nine(oper=''): return 9 if oper=='' else operation(9, oper)
def operation(numb, oper):
	if oper[0]=='*':
		return numb*int(oper[1])
	elif oper[0]=='+':
		return numb+int(oper[1])
	elif oper[0]=='-':
		return numb-int(oper[1])
	elif oper[0]=='/':
		return int(numb/int(oper[1]))
def plus(numb): return '+'+str(numb)
def minus(numb): return '-'+str(numb)
def times(numb): return '*'+str(numb)
def divided_by(numb): return '/'+str(numb)

assert seven(times(five())) == 35


## Not mine solution
# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)

# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y
