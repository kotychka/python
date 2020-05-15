from tkinter import *
from tkcalendar import Calendar, DateEntry
import db_budg_back

window=Tk()

window.wm_title('Family budget')

## functions
def get_selected_row(event):
	global selected_tuple
	index=list1.curselection()[0]
	selected_tuple=list1.get(index)
	e1.delete(0,END)
	e1.insert(END,selected_tuple[1])
	e2.delete(0,END)
	e2.insert(END,selected_tuple[2])
	e3.delete(0,END)
	e3.insert(END,selected_tuple[3])
	e4.delete(0,END)
	e4.insert(END,selected_tuple[4])
	e5.delete(0,END)
	e5.insert(END,selected_tuple[5])
	e6.delete(0,END)
	e6.insert(END,selected_tuple[6])
	e7.delete(0,END)
	e7.insert(END,selected_tuple[7])
	e8.delete(0,END)
	e8.insert(END,selected_tuple[8])
	e9.delete(0,END)
	e9.insert(END,selected_tuple[9])

def view_command():
	list1.delete(0,END)
	for row in db_budg_back.view():
		list1.insert(END,row)

def search_command():
	list1.delete(0,END)
	for row in db_budg_back.search(date_val.get(), sum_val.get(), bank_val.get()):
		list1.insert(END,row)

def add_command():
	db_budg_back.insert(date_val.get(), sum_val.get(), bank_val.get(), section_val.get(), categ_val.get(), sub_cat_val.get(), sub_cat2_val.get(), comm_val.get(), comp_val.get())
	list1.delete(0,END)
	list1.insert(END,(date_val.get(), sum_val.get(), bank_val.get(), section_val.get(), categ_val.get(), sub_cat_val.get(), sub_cat2_val.get(), comm_val.get(), comp_val.get()))

def del_command():
	db_budg_back.delete(selected_tuple[0])
	view_command()

def update_command():
	db_budg_back.update(selected_tuple[0],date_val.get(), sum_val.get(), bank_val.get(), section_val.get(), categ_val.get(), sub_cat_val.get(), sub_cat2_val.get(), comm_val.get(), comp_val.get())
	view_command()

def clear_command():
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)
	e5.delete(0,END)
	e6.delete(0,END)
	e7.delete(0,END)
	e8.delete(0,END)
	e9.delete(0,END)


## labels
l1=Label(window,text='Date')
l1.grid(row=0,column=0)

l2=Label(window,text='Sum')
l2.grid(row=0,column=2)

l3=Label(window,text='Bank')
l3.grid(row=0,column=4)

l4=Label(window,text='Section')
l4.grid(row=1,column=0)

l5=Label(window,text='Category')
l5.grid(row=1,column=2)

l6=Label(window,text='Sub categ')
l6.grid(row=1,column=4)

l7=Label(window,text='Sub categ2')
l7.grid(row=2,column=0)

l8=Label(window,text='Comment')
l8.grid(row=2,column=2)

l9=Label(window,text='Company')
l9.grid(row=2,column=4)


## buttons
b1=Button(window,text='View all', width=10,command=view_command)
b1.grid(row=0,column=6)

b2=Button(window,text='Search', width=10, command=search_command)
b2.grid(row=0,column=7)

b3=Button(window,text='Add', width=10, command=add_command)
b3.grid(row=1,column=6)

b4=Button(window,text='Update', width=10, command=update_command)
b4.grid(row=1,column=7)

b5=Button(window,text='Delete', width=10, command=del_command)
b5.grid(row=2,column=6)

b6=Button(window,text='Close', width=10, command=window.destroy)
b6.grid(row=2,column=7)

b7=Button(window,text='Clear',width=10, command=clear_command)
b7.grid(row=3,column=7)


## fields for entry
date_val=StringVar()
e1=Entry(window,textvariable=date_val)
e1.grid(row=0,column=1)

sum_val=StringVar()
e2=Entry(window, textvariable=sum_val)
e2.grid(row=0,column=3)

bank_val=StringVar()
e3=Entry(window, textvariable=bank_val)
e3.grid(row=0,column=5)

section_val=StringVar()
e4=Entry(window, textvariable=section_val)
e4.grid(row=1,column=1)

categ_val=StringVar()
e5=Entry(window, textvariable=categ_val)
e5.grid(row=1,column=3)

sub_cat_val=StringVar()
e6=Entry(window, textvariable=sub_cat_val)
e6.grid(row=1,column=5)

sub_cat2_val=StringVar()
e7=Entry(window, textvariable=sub_cat2_val)
e7.grid(row=2,column=1)

comm_val=StringVar()
e8=Entry(window, textvariable=comm_val)
e8.grid(row=2,column=3)

comp_val=StringVar()
e9=Entry(window, textvariable=comp_val)
e9.grid(row=2,column=5)

## listbox
list1=Listbox(window,height=6,width=150)
list1.grid(row=4,column=0,rowspan=6,columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=4,column=6,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# binding
list1.bind('<<ListboxSelect>>',get_selected_row)

## 



window.mainloop()