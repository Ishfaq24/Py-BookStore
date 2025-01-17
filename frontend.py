"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend
from tkinter import messagebox
from backend import Database


database=Database("books.db")


def get_selected_row(event):
    try:
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
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def update_command():
    global selected_tuple
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()

    


def delete_command():
    global selected_tuple
    if selected_tuple:
        database.delete(selected_tuple[0])
        messagebox.showinfo("Success", "Record deleted successfully.")
    else:
        messagebox.showwarning("No Selection", "Please select an item to delete.")
    view_command()    
        
    


window =Tk()


window.wm_title("Book Store")


l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2) 

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.config(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window, text="View all",command=view_command, width=12)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", command=search_command, width=12)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", command=add_command, width=12)
b3.grid(row=4, column=3)

b4=Button(window, text="Update Selected", command=update_command, width=12)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete selected", command=delete_command, width=12)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", command=window.destroy, width=12)
b6.grid(row=7, column=3)


window.mainloop()