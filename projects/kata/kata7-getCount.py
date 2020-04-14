def getCount(inputStr):
    num_vowels = 0
    # your code here
    for letter in inputStr:
        if 'aeio'.find(letter) != -1:
            num_vowels+=1
            print(letter)
    
    return num_vowels

print(getCount('abracadabra'))
print('smth'*2)
# assert getCount("abracadeabra") == 6