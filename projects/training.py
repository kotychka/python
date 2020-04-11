### Not mine solution
def digital_root(n):
    while n>10:
        n = sum([int(i) for i in str(n)])
    print(n)

digital_root(16) #7
digital_root(456) #6
digital_root(493193) #2