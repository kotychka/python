def get_middle(s):
    #your code here
    if len(s)%2:
        return s[len(s)//2]
    else:
        return s[(len(s)//2-1):(len(s))//2+1]

## Not mine solution
# def get_middle(s):
# 	return s[(len(s)-1)//2:len(s)//2+1] 

assert get_middle("test")=="es"
assert get_middle("testing")=="t"
assert get_middle("middle")=="dd"
assert get_middle("A")=="A"
assert get_middle("of")=="of"

