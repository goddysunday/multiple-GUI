from tkinter import *
from tkinter import messagebox
import sqlite3

def check():
    window = Tk()
    window.title("Data are as follows")
    window.geometry("300x350")
    window.maxsize(300,250)
    window.minsize(300,250)
    button1 = Button(window, text = "Show Records", fg = "white", bg = "brown",
                        font = "time 15 bold", width = 16, command = show)
    button1.place(x= 50, y = 50)

    button2 = Button(window, text = "Put Records", fg = "white", bg = "brown",
                        font = "time 15 bold", width = 16, command = put)
    button2.place(x= 50, y = 150)

    window.mainloop()

def put():
    root = Tk()
    root.title("Data are as follows")
    root.geometry("300x350")
    root.maxsize(300,250)
    root.minsize(300,250)

    global e1
    l1 = Label(root, text = "Enter Name", font = "time 15 bold")
    l1.place(x = 50, y = 20)
    
    e1 = Entry(root, width = 18, bd = 3, font = "time 15 bold")
    e1.place(x = 50, y =70)
    button1 = Button(root, text = "Enter", fg = "white", bg = "brown",
                        font = "time 15 bold", width = 16, command = enter)
    button1.place(x= 50, y = 140)

def enter():
    name = e1.get()
    conn = sqlite3.connect("project.db")
    c = conn.cursor()
    #c.execute(''' CREATE TABLE P (name TEXT )''')
    c.execute("INSERT INTO P VALUES('"+name+"')")
    messagebox.showinfo("Information", "Your Record Is Inserted")
    conn.commit()
    conn.close()

def show():
    roat = Tk()
    roat.title("Data are as follows")
    roat.geometry("300x350")
    roat.maxsize(300,350)
    roat.minsize(300,350)
    conn = sqlite3.connect("project.db")
    c = conn.cursor()
    c.execute("SELECT * FROM P")
    r = c.fetchall()
    num = 2
    p1 = Label(roat, text = "Name", font = "time 15 bold" ,justify = LEFT)
    p1.grid(row = 1, column = 0,  padx = 10, pady = 10)
    for i in r:
        p = Label(roat, text = i[0], font = "time 15 bold", fg = "blue" ,justify = LEFT)
        p.grid(row = num, column = 0,  padx = 10, pady = 10)
        num = num + 1 
    conn.commit()
    conn.close()

check()    
