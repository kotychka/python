# solution("camelCasing")  ==  "camel Casing"

def solution(s):
	#transform to array
	sol = list(s)
	length = len(sol)
	i = 0
	#finding the breaking point    
	while i <= length-1:
	    if sol[i].isupper() and sol[i-1] != ' ':
	    	break_point = i
	    	sol.insert(break_point, ' ')
	    	length = len(sol)
	    	i+=2
	    else:
	    	i+=1
	#transform to str
	s = ''.join(sol)
	print(s)

solution('camelCasing')
solution("helloWorld")
solution("breakCamelCase")
solution('make Eye Old GiveSee')
solution('dayVerbsRightHaveSee')


# Not mine solution
# def solution(s):
#     newStr = ""
#     for letter in s:
#         if letter.isupper():
#             newStr += " "
#         newStr += letter
#     return newStr