# ([1,2,3,4,5])  =>  [1,1,2,3,4]
# ([4,2,1,3,5])  =>  [1,1,2,3,4]
# ([2,3,4,5,6])  =>  [1,2,3,4,5]
# ([2,2,2])      =>  [1,2,2]
# ([42])         =>  [1]

def sort_number(a): 
    # your code here
    # res_a = []
    # for i in range(0, len(a)):
    # 	if a[i] == max(a):
    # 		res_a.append(i)
    # 		break
    
    if max(a) == 1:
    	a.sort()
    	a = a[1:len(a)+1]
    	a.append(2)
    else:
    	a.remove(max(a))
    	a.append(1)
    a.sort()
    print(a)

sort_number([6,2,3,4,5])
sort_number([4,2,1,3,5])
sort_number([2,3,4,5,6])
sort_number([1, 1, 1])
sort_number([42])

# Not mine solution
# def sort_number(a): 
#     a = sorted(a)
#     if a[len(a)-1] != 1:
#         a[len(a)-1] = 1
#     else:
#         a[len(a)-1] = 2
    
#     return sorted(a)