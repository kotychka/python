
filename = input('Write the filename to choose: ')
content = input('Write whatever you want: ')

file = open(filename, 'w')
file.write(content)
file.close()