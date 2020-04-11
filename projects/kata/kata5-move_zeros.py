#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    #your code here
    q = len(array)-1
    q_0 = array.count(0)
    q_f = str(array).count('False')
    new_array = []
    i=0
    while i <= q:
    	if array[i]==None:
    		new_array.append(None)
    	elif array[i] == '0':
    		new_array.append(array[i])
    	elif str(array[i]) != '0' and str(array[i]) != '0.0':
    		new_array.append(array[i])
    	i+=1
    i = 1
    while i <= q_0 - q_f:
    	new_array.append(0)
    	i+=1
    print(new_array)


# move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])	#["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
move_zeros( ['y', -6, 9, 0, 7, -4, 1, 2, 'c', 0, -4, -9, '0', -3, 'a', 0, -3, 'x', 10, 'x', -1, False, -8, 'c', 3])
# ['y', -6, 9, 7, -4, 1, 2, 'c', -4, -9, '0', -3, 'a', -3, 'x', 10, 'x', -1, False, -8, 'c', 3, 0, 0, 0]

# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
# move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])	#[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]


## Not mine solution
# def move_zeros(array):
#     return sorted(array, key=lambda x: x == 0 and x is not False)


# def move_zeros(array):
#     return sorted(array, key=lambda x: x==0 and type(x) is not bool)


# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))

