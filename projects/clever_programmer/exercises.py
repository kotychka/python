def is_even(numb):
	# return False if numb%2 else True
	return numb%2 == 0

def test_is_even():
	assert is_even(2) == True
	assert is_even(3) == False
	assert is_even(80) == True
	print('Even is correct')

test_is_even()

def string_lenght(string):
	return len(string)

print(string_lenght('hellop'))

def last_letter(string):
	return string[-1]

def test_last_letter():
	assert last_letter('hello!') == '!'
	assert last_letter('101') == '1'
	print('Last_letter is correct')

test_last_letter()

race = {
	'Usain' : 1,
	'Me' : 2,
	'Qazi' : 3
}

def choice_to_number(numb):
	race = {1 : 'Usain', 2 : 'Me', 3 : 'Qazi'}
	return race[numb]

def number_to_choice(name):
	race = {'Usain' : 1, 'Me' : 2, 'Qazi' : 3}
	return race[name]

print(choice_to_number(1))
print(number_to_choice('Me'))

