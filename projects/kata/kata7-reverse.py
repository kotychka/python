def reverse(lst):
    empty_list = list()            # use this!
    for item in lst:
    	empty_list.insert(0,item) 
    return empty_list

assert reverse(list([1,None,14,"two"])) == ["two",14,None,1]
    