###Arguments (Other languages)
# First argument (required): the original string to be converted.
# Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.

def title_case(title, minor_words=''):
    title_list = title.split(' ')
    minor_list = minor_words.lower().split(' ')
    new_title = ''
    i = 0
    while i <= len(title_list)-1:
    	if i == 0:
    		new_title += title_list[i].capitalize()
    	elif title_list[i].lower() not in minor_list:
    		new_title += ' ' + title_list[i].capitalize()
    	else:
    		new_title += ' ' + title_list[i].lower()
    	i+=1
    print(new_title)

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'

## Not mine solution
# def title_case(title, minor_words=''):
#     title = title.capitalize().split()
#     minor_words = minor_words.lower().split()
#     return ' '.join([word if word in minor_words else word.capitalize() for word in title])


#     def title_case(title, minor_words=''):
#     title, minor_words = title.lower().split(), minor_words.lower().split()
#     for i in range(len(title)):
#         if i == 0 or title[i] not in minor_words:
#             title[i] = title[i].capitalize()
#     return ' '.join(title)