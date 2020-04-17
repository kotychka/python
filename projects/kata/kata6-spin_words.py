#Write a function that takes in a string of one or more words, and returns the same string, 
#but with all five or more letter words reversed (Just like the name of this Kata). 
#Strings passed in will consist of only letters and spaces. 
#Spaces will be included only when more than one word is present.

def spin_words(sentence):
    # Your code goes here
    new_sent = []
    for word in sentence.split(' '):
    	if len(word) >= 5:
    		new_sent.append(word[::-1])
    	else:
    		new_sent.append(word)
    return ''.join(new_sent) if len(new_sent)==1 else ' '.join(new_sent)
    
# print(spin_words('Welcome'))
# print(spin_words("Hey Welcome"))

assert spin_words("Welcome") == "emocleW"
assert spin_words("Hey Welcome") == "Hey emocleW"