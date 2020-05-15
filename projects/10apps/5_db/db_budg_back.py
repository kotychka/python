import sqlite3

def connect():
	conn=sqlite3.connect('budget.db')
	cur=conn.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS operations (id INTEGER PRIMARY KEY AUTOINCREMENT, op_date date, sum integer, bank text, section text, category text, sub_categ text, sub_categ2 text, comment text, company text)')
	conn.commit()
	conn.close()

def insert(op_date, sum, bank, section, category, sub_categ, sub_categ2, comment, company):
	conn=sqlite3.connect('budget.db')
	cur=conn.cursor()
	cur.execute('INSERT INTO operations VALUES (NULL,?,?,?,?,?,?,?,?,?)', (op_date, sum, bank, section, category, sub_categ, sub_categ2, comment, company))
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect('budget.db')
	cur=conn.cursor()
	cur.execute('SELECT * FROM operations')
	rows=cur.fetchall()
	conn.close()
	return rows

# def search(op_date='', sum='', bank='sber', selection='', category='', sub_categ='', sub_categ2='', comment='', company=''):
# 	conn=sqlite3.connect('budget.db')
# 	cur=conn.cursor()
# 	cur.execute('SELECT * FROM operations WHERE op_date=? OR sum=? OR bank=? OR selection=? OR category=? OR sub_categ=? OR sub_categ2=? OR comment=? OR company=?', (op_date, sum, bank, selection, category, sub_categ, sub_categ2, comment, company))
# 	rows=cur.fetchall()
# 	conn.close()
# 	return rows

def search(op_date='',sum='', bank=''):
	conn=sqlite3.connect('budget.db')
	cur=conn.cursor()
	cur.execute('SELECT * FROM operations WHERE op_date=? OR sum=? OR bank=?', (op_date,sum,bank))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn=sqlite3.connect('budget.db')
	cur=conn.cursor()
	cur.execute('DELETE FROM operations WHERE id=?', (id,))
	conn.commit()
	conn.close()

def update(id, op_date, sum, bank, section, category, sub_categ, sub_categ2, comment, company):
	conn=sqlite3.connect('budget.db')
	cur=conn.cursor()
	cur.execute('UPDATE operations SET op_date=?, sum=?, bank=?, section=?, category=?, sub_categ=?, sub_categ2=?, comment=?, company=? WHERE id=?', (op_date, sum, bank, section, category, sub_categ, sub_categ2, comment, company,id))
	conn.commit()
	conn.close()



connect()
# insert('10.01.2020',5000,'spb','life','kids','','','','')
# print(update(1,op_date='10.10.2020'))
