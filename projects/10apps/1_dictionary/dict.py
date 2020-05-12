import json
from difflib import get_close_matches

data = json.load(open("data.json"))
print()
print()
word = input('\t'+'Enter a word: (If you want to quit the dictionary enter Q) ')
print()
print()

def translate(w):

	if w in data:
		return data[w]
	elif w.lower() in data:
		return data[w.lower()]
	elif w.upper() in data:
		return data[w.upper()]
	elif w.capitalize() in data:
		return data[w.capitalize()]
	elif len(get_close_matches(w, data.keys())) > 0:
		yn = input('\t'+'Did you mean %s instead? Enter Y if yes, or N if no.' % get_close_matches(w, data.keys())[0].upper())
		print()
		print()	
		if yn.lower() == 'y':
			return data[get_close_matches(w, data.keys())[0]]
		elif yn.lower() == 'n':
			return '\t'+"The word doesn't exist. Please double check it."
		else:
			return '\t'+"We didn't understand your query."
	else:
		return '\t'+"The word doesn't exist. Please double check it."


while word.lower() != 'q':
	output = translate(word)

	if type(output) == list:
		for item in output:
			print(item)
	else:
		print(output)

	print()
	print()
	word = input('\t'+'Enter a word: (If you want to quit the dictionary enter Q) ')
	print()
	print()