def to_alternating_case(string):
    #your code here
    string_list = list(string)
    length = len(string_list)
    i = 0
    while i <= length-1:
	    if string_list[i].islower():
	    	string_list[i] = string_list[i].upper()
	    elif string_list[i].isupper():
	    	string_list[i] = string_list[i].lower()
	    i+=1
    string = ''.join(string_list)
    print(string)    

# string = input('Write something in different case: ')
# to_alternating_case(string)