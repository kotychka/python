import sys
sys.path.insert(1, '../../../keys/')
import mysql_ardit
import mysql.connector

con = mysql.connector.connect(
	user = mysql_ardit.user,
	password = mysql_ardit.password,
	host = mysql_ardit.host,
	database = mysql_ardit.database)
cursor = con.cursor()

print()
print()
word = input('\t'+"Enter a word: (If you want to quit the dictionary enter Q) ")
print()
print()


while word.lower() != 'q':
	query = cursor.execute('SELECT * FROM Dictionary WHERE Expression = "%s" ' % word)
	results = cursor.fetchall()

	if results:
		for result in results:
			print(result[1])
	else:
		print("The word wasn't found!")

	print()
	print()
	word = input('\t'+'Enter a word: (If you want to quit the dictionary enter Q) ')
	print()
	print()